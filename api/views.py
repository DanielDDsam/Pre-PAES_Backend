from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from api.serializers import *
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from api.models import *
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, logout
from api.renderers import UserRenderer
from django_filters.rest_framework import DjangoFilterBackend
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.conf import settings
from django.core.mail import send_mail
import openai, os
from dotenv import load_dotenv
import requests
import json
import wolframalpha
from xml.etree import ElementTree
load_dotenv()

# Create your views here.

api_key = os.getenv("OPENAI_KEY", None)
puntajes = {
    "Universidad de Chile": [
    { "programa": "Arquitectura", "puntaje": 728.30 },
    { "programa": "DISEÑO", "puntaje": 695.05 },
    { "programa": "GEOGRAFÍA", "puntaje": 608.10 },
    { "programa": "ACTUACIÓN TEATRAL", "puntaje": 718.98 },
    { "programa": "ARTES VISUALES", "puntaje": 701.90 },
    { "programa": "DANZA", "puntaje": 749.08 },
    { "programa": "DISEÑO TEATRAL", "puntaje": 627.95 },
    { "programa": "INGENIERÍA EN SONIDO", "puntaje": 782.10 },
    { "programa": "TEORÍA DE LA MÚSICA", "puntaje": 667.70 },
    { "programa": "TEORÍA E HISTORIA DEL ARTE", "puntaje": 612.70 },
    { "programa": "BIOLOGÍA CON MENCIÓN EN MEDIO AMBIENTE", "puntaje": 724.30 },
    { "programa": "INGENIERÍA EN BIOTECNOLOGÍA MOLECULAR", "puntaje": 831.60 },
    { "programa": "LIC. EN CIENCIAS MENCIÓN BIOLOGÍA", "puntaje": 713.15 },
    { "programa": "LIC. EN CIENCIAS MENCIÓN FÍSICA", "puntaje": 739.10 },
    { "programa": "LIC. EN CIENCIAS MENCIÓN MATEMÁTICAS", "puntaje": 617.30 },
    { "programa": "LIC. EN CIENCIAS MENCIÓN QUÍMICA", "puntaje": 488.10 },
    { "programa": "PEDAGOGÍA EN ED. MEDIA EN BIOLOGÍA Y QUÍMICA", "puntaje": 570.40 },
    { "programa": "PEDAGOGÍA EN ED. MEDIA EN MATEMÁTICAS Y FÍSICA", "puntaje": 524.90 },
    { "programa": "QUÍMICA AMBIENTAL", "puntaje": 539.65 },
    { "programa": "INGENIERÍA AGRONÓMICA", "puntaje": 603.45 },
    { "programa": "INGENIERÍA EN RECURSOS NATURALES RENOVABLES", "puntaje": 635.05 },
    { "programa": "INGENIERÍA Y CIENCIAS - PLAN COMÚN", "puntaje": 818.35 },
    { "programa": "INGENIERÍA EN RECURSOS HÍDRICOS", "puntaje": 523.60 },
    { "programa": "INGENIERÍA FORESTAL", "puntaje": 573.90 },
    { "programa": "BIOQUÍMICA", "puntaje": 778.80 },
    { "programa": "INGENIERÍA EN ALIMENTOS", "puntaje": 558.00 },
    { "programa": "QUÍMICA", "puntaje": 621.90 },
    { "programa": "QUÍMICA Y FARMACIA", "puntaje": 727.10 },
    { "programa": "ANTROPOLOGÍA-ARQUEOLOGÍA", "puntaje": 761.65 },
    { "programa": "PEDAGOGÍA EN EDUCACIÓN PARVULARIA", "puntaje": 648.85 },
    { "programa": "PSICOLOGÍA", "puntaje": 864.05 },
    { "programa": "SOCIOLOGÍA", "puntaje": 740.55 },
    { "programa": "TRABAJO SOCIAL", "puntaje": 711.40 },
    { "programa": "MEDICINA VETERINARIA", "puntaje": 725.30 },
    { "programa": "CINE Y TELEVISIÓN", "puntaje": 751.30 },
    { "programa": "PERIODISMO", "puntaje": 748.30 },
    { "programa": "DERECHO", "puntaje": 830.80 },
    { "programa": "CONTADOR AUDITOR", "puntaje": 703.65 },
    { "programa": "INGENIERÍA EN INFORMACIÓN Y CONTROL DE GESTIÓN", "puntaje": 700.90 },
    { "programa": "INGENIERÍA COMERCIAL", "puntaje": 777.95 },
    { "programa": "ESTUDIOS INTERNACIONALES", "puntaje": 822.60 },
    { "programa": "FILOSOFÍA", "puntaje": 523.40 },
    { "programa": "HISTORIA", "puntaje": 661.20 },
    { "programa": "LINGÜÍSTICA Y LITERATURA", "puntaje": 668.50 },
    { "programa": "LINGÜÍSTICA Y LITERATURA INGLESAS", "puntaje": 690.90 },
    { "programa": "PEDAGOGÍA EN EDUCACIÓN BÁSICA", "puntaje": 677.15 },
    { "programa": "ADMINISTRACIÓN PÚBLICA", "puntaje": 708.20 },
    { "programa": "CIENCIA POLÍTICA", "puntaje": 791.60 },
    { "programa": "ENFERMERÍA", "puntaje": 755.25 },
    { "programa": "FONOAUDIOLOGÍA", "puntaje": 599.35 },
    { "programa": "KINESIOLOGÍA", "puntaje": 743.30 },
    { "programa": "MEDICINA", "puntaje": 900.00 },
    { "programa": "NUTRICIÓN Y DIETÉTICA", "puntaje": 695.60 },
    { "programa": "OBSTETRICIA Y PUERICULTURA", "puntaje": 754.55 },
    { "programa": "TECNOLOGÍA MÉDICA", "puntaje": 767.60 },
    { "programa": "TERAPIA OCUPACIONAL", "puntaje": 660.60 },
    { "programa": "ODONTOLOGÍA", "puntaje": 772.40 },
    { "programa": "PROGRAMA ACADÉMICO DE BACHILLERATO", "puntaje": 741.05 }
    ]
    }


from rest_framework.response import Response

class WolframAlphaQuery(APIView):
    def post(self, request):
        app_id = '6Y2Q4G-94JAJ2HAGG'  # Reemplaza con tu ID de la API de Wolfram Alpha
        
        client = wolframalpha.Client(app_id)
        input_query = request.data.get('user_input') # Reemplaza con tu consulta específica
        url = "http://api.wolframalpha.com/v2/query?appid="+app_id+"&input=solve+"+input_query+"&podstate=Result__Step-by-step%20solution&format=image"
       

        response = requests.get(url)
        xml_data = ElementTree.fromstring(response.content)
        image_elements = xml_data.findall(".//img")
        image_urls = [img.get("src") for img in image_elements]

        if input_query is not None:
            return Response({"response": image_urls}, status=status.HTTP_200_OK)
        else:
            return Response({'errors': {'error_de_campo': ['Promt vacio']}})


      


class chatbot(APIView):

    def post(self, request):
        chatbot_response = None
        if api_key is not None and request.method == 'POST':
            openai.api_key = api_key
            user_input = request.data.get('user_input')
            prompt = user_input
            #contexto del asistente 
            messages = [{"role" : "system",
                         "content": "Redacta mejor el siguiente texto. No vas a responder preguntas." }]
            messages.append({"role" : "user","content": prompt})
            response = openai.ChatCompletion.create(
                model = 'gpt-3.5-turbo',
                messages = messages,
             
                max_tokens=250,
                temperature=0.5
            )
            chatbot_response = response.choices[0].message.content
            messages.append({"role" : "assistant","content": chatbot_response})

            
        if chatbot_response is not None:
            return Response({"response": chatbot_response}, status=status.HTTP_200_OK)
        else:
            return Response({'errors': {'error_de_campo': ['Promt vacio']}},
                                status=status.HTTP_404_NOT_FOUND)

class chatbotPrueba(APIView):

    def post(self, request):
        chatbot_response = None
        if api_key is not None and request.method == 'POST':
            openai.api_key = api_key
            user_input = request.data.get('user_critiques')
            prompt = user_input
            #contexto del asistente 
            messages = [{"role" : "system",
                         "content": "Tu mision es detectar los errores de redaccion de texto. No vas a responder preguntas." }]
            messages.append({"role" : "user","content": prompt})
            response = openai.ChatCompletion.create(
                model = 'gpt-3.5-turbo',
                messages = messages,
             
                max_tokens=250,
                temperature=0.5
            )
            chatbot_response = response.choices[0].message.content
            messages.append({"role" : "assistant","content": chatbot_response})

            
        if chatbot_response is not None:
            return Response({"response": chatbot_response}, status=status.HTTP_200_OK)
        else:
            return Response({'errors': {'error_de_campo': ['Promt vacio']}},
                                status=status.HTTP_404_NOT_FOUND)

#funcion para obtener jwt para el usuario cuando hace login
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

#views para el manejo de los user

class UsersRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.filter().order_by('pk')
    serializer_class = UserSerializer


class UsersListCreate(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response({'token': token, 'msg': 'Inicio de sesión exitoso','status': 'ok','user_id': user.id }, status=status.HTTP_200_OK)
        else:
            return Response({'errors': {'error_de_campo': ['Email o contraseña invalidos']}},
                            status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):

    def post(self, request):
        logout(request)
        return Response({'msg': 'Se cerro la sesión con éxito'}, status=status.HTTP_200_OK)


class ChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def patch(self, request, format=None):
        serializer = PasswordChangeSerializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Contraseña cambiada exitosamente'}, status=status.HTTP_200_OK)


class UserProfileView(APIView):
    renderer_classes = [UserRenderer,]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Link para reiniciar contraseña enviado'}, status=status.HTTP_200_OK)


class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid,'token':token})
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'Cambio de contraseña exitoso'}, status=status.HTTP_200_OK)


#demas views
class EssayList(generics.ListAPIView):
    queryset = Essay.objects.filter().order_by('pk')
    serializer_class = EssaySerializer


class EssayCreate(generics.CreateAPIView):
    queryset = Essay.objects.filter().order_by('pk')
    serializer_class = EssaySerializer


class EssayRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Essay.objects.filter().order_by('pk')
    serializer_class = EssaySerializer


class QuestionCreate(generics.CreateAPIView):
    queryset = Question.objects.filter().order_by('pk')
    serializer_class = QuestionCreateSerializer


class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','essays', 'question','subject','link_resolution']


class QuestionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.filter().order_by('pk')
    serializer_class = QuestionSerializer


class AnswerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.filter().order_by('pk')
    serializer_class = AnswerSerializer


class AnswerList(generics.ListAPIView):
    queryset = Answer.objects.filter().order_by('pk')
    serializer_class = AnswerSerializer


class AnswerCreate(generics.CreateAPIView):
    queryset = Answer.objects.filter().order_by('pk')
    serializer_class = AnswerCreateSerializer


class QuestionsAlternativeAllView(generics.ListAPIView):
    serializer_class = QuestionsAlternativeAllSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','essays','subject']
    queryset = Question.objects.all()


class AnswerEssayUserView(generics.ListAPIView):
    serializer_class = AnswerEssayUserSerializer
    queryset = AnswerEssayUser.objects.filter(is_deleted=False).order_by('pk')


class UserEssayView(generics.CreateAPIView):
    serializer_class = EssayUserSerializer
    queryset = UserEssay.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SaveAnswersView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SaveAnswersSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'CREATED'}, status=status.HTTP_201_CREATED)


class UserEssayHistoryView(generics.ListAPIView):
    serializer_class = UserEssayHistorySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user_pk = self.kwargs['pk']
        return UserEssay.objects.filter(user_id=user_pk)