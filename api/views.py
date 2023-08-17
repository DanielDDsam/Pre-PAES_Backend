from rest_framework import generics
from rest_framework.views import APIView
from api.serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from api.models import *
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, logout
from api.renderers import UserRenderer
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models.functions import Random
import random
import math
# Create your views here.

#funcion para obtener jwt para el usuario cuando hace login
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)  # Genera un token de actualización para el usuario proporcionado

    return {
        'refresh': str(refresh),  # Convierte el token de actualización a una cadena y lo retorna
        'access': str(refresh.access_token),  # Convierte el token de acceso asociado al token de actualización a una cadena y lo retorna
    }


# Views para el manejo de usuarios

class UsersRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.filter().order_by('pk')  # Obtiene todos los usuarios ordenados por su clave primaria
    serializer_class = UserSerializer  # Serializador utilizado para la representación de los usuarios


class UsersListCreate(generics.ListCreateAPIView):
    queryset = Users.objects.all()  # Obtiene todos los usuarios
    serializer_class = UserSerializer  # Serializador utilizado para la representación de los usuarios

class RegisterView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)  # Serializador utilizado para validar y procesar los datos del formulario
        if serializer.is_valid():
            serializer.save()  # Guarda los datos del nuevo usuario en la base de datos
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Retorna los datos del usuario registrado en la respuesta con un código de estado 201 (CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Retorna los errores de validación en la respuesta con un código de estado 400 (BAD REQUEST)


class LoginView(APIView):
    renderer_classes = [UserRenderer]  # Clase de renderizado utilizada para la vista

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)  # Serializador utilizado para validar y procesar los datos del formulario
        serializer.is_valid(raise_exception=True)  # Valida los datos y lanza una excepción si no son válidos
        email = serializer.data.get('email')  # Obtiene el email del usuario del serializador
        password = serializer.data.get('password')  # Obtiene la contraseña del usuario del serializador
        user = authenticate(email=email, password=password)  # Autentica al usuario utilizando el email y la contraseña
        if user is not None:
            token = get_tokens_for_user(user)  # Obtiene el token de acceso para el usuario autenticado
            return Response({'token': token, 'msg': 'Inicio de sesión exitoso', 'status': 'ok','user_id':user.id, 'username':user.username}, status=status.HTTP_200_OK)  # Retorna el token de acceso en la respuesta con un mensaje de éxito y un código de estado 200 (OK)
        else:
            return Response({'errors': {'error_de_campo': ['Email o contraseña invalidos']}}, status=status.HTTP_404_NOT_FOUND)  # Retorna un mensaje de error en la respuesta con un código de estado 404 (NOT FOUND)


class LogoutView(APIView):

    def post(self, request):
        logout(request)  # Cierra la sesión del usuario
        return Response({'msg': 'Se cerro la sesión con éxito'},
                        status=status.HTTP_200_OK)  # Retorna un mensaje de éxito en la respuesta


class ChangePasswordView(APIView):
    renderer_classes = [UserRenderer]  # Clase de renderizado utilizada para la vista
    permission_classes = [IsAuthenticated]  # Clases de permisos requeridos para acceder a la vista

    def patch(self, request, format=None):
        serializer = PasswordChangeSerializer(data=request.data, context={
            'user': request.user})  # Serializador utilizado para validar y procesar los datos del formulario
        serializer.is_valid(raise_exception=True)  # Valida los datos y lanza una excepción si no son válidos
        return Response({'msg': 'Contraseña cambiada exitosamente'},
                        status=status.HTTP_200_OK)  # Retorna un mensaje de éxito en la respuesta

class ChangeProfilePasswordView(APIView):
    renderer_classes = [UserRenderer]  # Clase de renderizado utilizada para la vista
    permission_classes = [IsAuthenticated]  # Clases de permisos requeridos para acceder a la vista

    def patch(self, request, format=None):
        serializer = PasswordChangeProfileSerializer(data=request.data, context={
            'user': request.user})  # Serializador utilizado para validar y procesar los datos del formulario
        serializer.is_valid(raise_exception=True)  # Valida los datos y lanza una excepción si no son válidos
        return Response({'msg': 'Contraseña cambiada exitosamente'},
                        status=status.HTTP_200_OK)  # Retorna un mensaje de éxito en la respuesta


class UserProfileView(APIView):
    renderer_classes = [UserRenderer,]  # Clase de renderizado utilizada para la vista
    permission_classes = [IsAuthenticated]  # Clases de permisos requeridos para acceder a la vista

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)  # Serializador utilizado para convertir el objeto de usuario en datos JSON
        return Response(serializer.data, status=status.HTTP_200_OK)  # Retorna los datos del usuario en la respuesta


class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]  # Clase de renderizado utilizada para la vista

    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)  # Serializador utilizado para validar y procesar los datos del formulario
        serializer.is_valid(raise_exception=True)  # Valida los datos y lanza una excepción si no son válidos
        return Response({'msg': 'Link para reiniciar contraseña enviado'}, status=status.HTTP_200_OK)  # Retorna un mensaje de éxito en la respuesta


class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]  # Clase de renderizado utilizada para la vista

    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid,'token':token})  # Serializador utilizado para validar y procesar los datos del formulario
        serializer.is_valid(raise_exception=True)  # Valida los datos y lanza una excepción si no son válidos
        return Response({'msg':'Cambio de contraseña exitoso'}, status=status.HTTP_200_OK)  # Retorna un mensaje de éxito en la respuesta


class EssayList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]  # Clases de permisos requeridos para acceder a la vista
    queryset = MathType.objects.filter().order_by('pk')  # Consulta para obtener los ensayos ordenados por clave primaria
    serializer_class = EssaySerializer  # Clase serializadora utilizada


class EssayCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]  # Clases de permisos requeridos para acceder a la vista
    queryset = MathType.objects.filter().order_by('pk')  # Consulta para obtener los ensayos ordenados por clave primaria
    serializer_class = EssaySerializer  # Clase serializadora utilizada


class EssayRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]  # Clases de permisos requeridos para acceder a la vista
    queryset = MathType.objects.filter().order_by('pk')  # Consulta para obtener los ensayos ordenados por clave primaria
    serializer_class = EssaySerializer  # Clase serializadora utilizada


class QuestionCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Question.objects.filter().order_by('pk')  # Consulta para obtener las preguntas ordenadas por clave primaria
    serializer_class = QuestionCreateSerializer  # Clase serializadora utilizada


class QuestionList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Question.objects.all()  # Consulta para obtener todas las preguntas
    serializer_class = QuestionSerializer  # Clase serializadora utilizada

    filter_backends = [DjangoFilterBackend]  # Filtros aplicados a la vista
    filterset_fields = ['id', 'essays', 'question', 'subject', 'link_resolution']  # Campos permitidos para filtrar


class QuestionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Question.objects.filter().order_by('pk')  # Consulta para obtener las preguntas ordenadas por clave primaria
    serializer_class = QuestionSerializer  # Clase serializadora utilizada


class AnswerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Answer.objects.filter().order_by('pk')  # Consulta para obtener las respuestas ordenadas por clave primaria
    serializer_class = AnswerSerializer  # Clase serializadora utilizada


class AnswerList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Answer.objects.filter().order_by('pk')  # Consulta para obtener las respuestas ordenadas por clave primaria
    serializer_class = AnswerSerializer  # Clase serializadora utilizada


class AnswerCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Answer.objects.filter().order_by('pk')  # Consulta para obtener las respuestas ordenadas por clave primaria
    serializer_class = AnswerCreateSerializer  # Clase serializadora utilizada


class QuestionsAlternativeAllView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionsAlternativeAllSerializer  # Clase serializadora utilizada
    filter_backends = [DjangoFilterBackend]  # Filtros aplicados a la vista
    filterset_fields = ['id', 'type_question', 'subject']  # Campos permitidos para filtrar
    queryset = Question.objects.all()  # Consulta para obtener todas las preguntas


class AnswerEssayUserView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AnswerEssayUserSerializer  # Clase serializadora utilizada
    queryset = AnswerEssayUser.objects.filter(is_deleted=False).order_by('pk')  # Consulta para obtener las respuestas de los ensayos de usuario no eliminadas, ordenadas por clave primaria


class SaveAnswersView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)  # Permiso requerido para acceder a la vista
    serializer_class = SaveAnswersSerializer  # Clase serializadora utilizada

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})  # Crear una instancia del serializador con los datos de la solicitud
        serializer.is_valid(raise_exception=True)  # Validar los datos y lanzar una excepción en caso de que sean inválidos
        serializer.save()  # Guardar los datos
        return Response({'message': 'CREATED'}, status=status.HTTP_201_CREATED)  # Devolver una respuesta exitosa


class UserEssayHistoryView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserEssayHistorySerializer  # Clase serializadora utilizada
    permission_classes = (IsAuthenticated,)  # Permiso requerido para acceder a la vista

    def get_queryset(self):
        user_pk = self.kwargs['pk']  # Obtener el ID del usuario de los parámetros de la URL
        return CustomEssay.objects.filter(user_id=user_pk)  # Devolver los ensayos personalizados del usuario


class CustomEssayView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomEssay.objects.filter(is_deleted=False)  # Consulta para obtener los ensayos personalizados que no han sido eliminados
    serializer_class = CustomEssaySerializer  # Clase serializadora utilizada

    def perform_create(self, serializer):
        custom_essay = serializer.save()  # Guardar el ensayo personalizado
        response_data = {'id': custom_essay.id, 'message': 'CustomEssay creado exitosamente.'}
        return Response(response_data, status=status.HTTP_201_CREATED)  # Devolver una respuesta exitosa


class CustomEssayQuestionView(generics.ListCreateAPIView):
    queryset = CustomEssayQuestion.objects.filter(is_deleted=False)  # Consulta para obtener las relaciones entre ensayos personalizados y preguntas que no han sido eliminadas
    serializer_class = CustomEssayQuestionSerializer  # Clase serializadora utilizada
    permission_classes = (IsAuthenticated,)  # Permiso requerido para acceder a la vista



class CustomEssayResponseView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomEssay.objects.filter(is_deleted=False)
    serializer_class = CustomEssayResponseSerializer

#######################################################################################
class questionAnswers(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionAnswerSerializer
    filter_backends = [DjangoFilterBackend]
    
    def get_queryset(self):
        question_pk = self.kwargs['pk'] #obtenemos la pk de la url
        queryset = Question.objects.filter(id = question_pk)
        return queryset

class oneQuestion(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionOneSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated]  # Clases de permisos requeridos para acceder a la vista

    def get_queryset(self):
        #data = self.request.data.get('ids_a_evitar', [])
        #data = [int(id) for id in data if id.isdigit()]  # Convertir a enteros solo los elementos numéricos
        #queryset = Question.objects.filter(id = question_pk)
        #print(data)
        #UserQuestionState_ids = UserQuestionState.objects.values_list('id', flat=True) #agregar el usuario a que hace referencia
        #  
        user = self.request.user
        print(user.id)
        UserQuestionState_ids = UserQuestionState.objects.filter(users_id = user.id).values_list('id', flat=True) #agregar el usuario a que hace referencia 
        print('user question')
        print(UserQuestionState_ids)

        if UserQuestionState_ids:
            queryset = Question.objects.all().exclude(id__in=UserQuestionState_ids).order_by('?') #agregar el else
            #print(queryset.first())
        else:
            queryset = Question.objects.all().order_by('?')
        return queryset

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset().first()
        serializer = QuestionOneSerializer(queryset) 
        return Response(serializer.data)

class oneQuestionRules(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionOneSerializer
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):

        user = self.request.user#obtenemos el usuario actual 
        UserQuestionState_ids = UserQuestionState.objects.filter(users_id = user.id).values_list('id', flat=True) #obtenemos los ids de las preguntas contestadas 
        pregunta = self.obtener_pregunta(user)#pasamos el usuario para obtener una pregunta
        
        if pregunta == 'nueva':
            if UserQuestionState_ids:#vemos si ya contesto alguna pregunta
                queryset = Question.objects.all().exclude(id__in=UserQuestionState_ids).order_by('?') #sacamos una pregunta que no este entre las ya contestadas
                #print(queryset.first())
            else:
                queryset = Question.objects.all().order_by('?')
        else:
            queryset = Question.objects.filter(id=pregunta.question_id) #si la pregunta no es nueva, es reforzar o correcta la obtenemos 
        return queryset

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        print('queryset')
        queryset = self.get_queryset().first()
        serializer = QuestionOneSerializer(queryset) 
        print(queryset)
        return Response(serializer.data)
    
    def obtener_pregunta(self, user):
    # Contadores de preguntas correctas y reforzar
        create_data = UserQuestionState.objects.filter(users_id = user.id).order_by('created') #obtemos las preguntas ordenadas por orden de creación
        update_data = UserQuestionState.objects.filter(users_id = user.id).order_by('updated') #obtemos las preguntas ordenadas por orden de modificacion 
        allquestions = UserQuestionState.objects.filter(users_id = user.id) #las obtenemos todas
 
        todos_los_elementos = list(create_data)[-2:] + list(update_data)[-2:] #obtenemos las 2 ultimas creadas y modificadoas
        todos_los_elementos.sort(key=lambda x: x.created if x.created else x.updated, reverse=True) #se ordena por la fecha mas actual primero para ver las utimas 2 contestadas
        questionState = []
        questionState.extend(todos_los_elementos)
        
        for i in range(len(todos_los_elementos)): #eliminamos las preguntas repetidas
            
            if(i == 0):
                if (todos_los_elementos[i] == todos_los_elementos[i+1]): #si la primera pregunta tambien es la segunda entonces eliminamos la segunda
                    del questionState[i+1]
            else:
                if (todos_los_elementos[0] == todos_los_elementos[i]): 
                    del questionState[i]
        #en resumen dejamos las 2 preguntas contestadas recientemente, verificando que no sean las mismas

        print(questionState)

        preguntas_correctas = sum(1 for pregunta in allquestions if pregunta.state == 'Correcta')
        preguntas_erroneas = sum(1 for pregunta in allquestions if pregunta.state == 'Reforzar')
        print("Preguntas correctas:", preguntas_correctas)
        print("Preguntas para reforzar:", preguntas_erroneas)

        # Verificar si se han respondido al menos 3 preguntas erróneas y 3 preguntas para reforzar
        if preguntas_correctas + preguntas_erroneas >= 6:
            # Obtener las últimas 2 respuestas del usuario

            ultimas_respuestas = [pregunta.state for pregunta in questionState[-2:]]
            # Probabilidad de cambiar una pregunta "correcta" a "reforzar" o "nueva"
            if ultimas_respuestas == ['Correcta', 'Correcta'] and random.random() < 0.7:
                # Cambiar una pregunta "correcta" a "reforzar"
                preguntas_erroneas_list = [pregunta for pregunta in allquestions if pregunta.state == 'Reforzar']
                pregunta_seleccionada = random.choice(preguntas_erroneas_list)
                pass
            elif ultimas_respuestas == ['Reforzar', 'Reforzar'] and random.random() < 0.7:
                # Cambiar una pregunta "errónea" a "correcta"
                preguntas_correctas_list = [pregunta for pregunta in allquestions if pregunta.state == 'Correcta']
                pregunta_seleccionada = random.choice(preguntas_correctas_list)
                pass
            else:
                # Indicar que la pregunta debe ser nueva
                return 'nueva'
        else:
            # Indicar que la pregunta debe ser nueva
            return 'nueva'
        #print(pregunta_seleccionada.id)
        return pregunta_seleccionada

class oneQuestionRulesPrePaes(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionOneSerializer
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):

        user = self.request.user#obtenemos el usuario actual 
        UserQuestionState_ids = UserQuestionState.objects.filter(users_id = user.id).values_list('id', flat=True) #obtenemos los ids de las preguntas contestadas 
        pregunta = self.obtener_pregunta(user)#pasamos el usuario para obtener una pregunta
        
        if pregunta == 'nueva':
            if UserQuestionState_ids:#vemos si ya contesto alguna pregunta
                queryset = Question.objects.all().exclude(id__in=UserQuestionState_ids).order_by('?') #sacamos una pregunta que no este entre las ya contestadas
                #print(queryset.first())
            else:
                queryset = Question.objects.all().order_by('?')
        else:
            queryset = Question.objects.filter(id=pregunta.question_id) #si la pregunta no es nueva, es reforzar o correcta la obtenemos 
        return queryset

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        print('queryset')
        queryset = self.get_queryset().first()
        serializer = QuestionOneSerializer(queryset) 
        print(queryset)
        return Response(serializer.data)
    
    def save_obtain_question(self,request):
        pass
    
    def obtener_pregunta(self, user):
    # Contadores de preguntas correctas y reforzar
        create_data = UserQuestionState.objects.filter(users_id = user.id).order_by('created') #obtemos las preguntas ordenadas por orden de creación
        update_data = UserQuestionState.objects.filter(users_id = user.id).order_by('updated') #obtemos las preguntas ordenadas por orden de modificacion 
        allquestions = UserQuestionState.objects.filter(users_id = user.id) #las obtenemos todas
 
        todos_los_elementos = list(create_data)[-2:] + list(update_data)[-2:] #obtenemos las 2 ultimas creadas y modificadoas
        todos_los_elementos.sort(key=lambda x: x.created if x.created else x.updated, reverse=True) #se ordena por la fecha mas actual primero para ver las utimas 2 contestadas
        questionState = []
        questionState.extend(todos_los_elementos)
        
        for i in range(len(todos_los_elementos)): #eliminamos las preguntas repetidas
            
            if(i == 0):
                if (todos_los_elementos[i] == todos_los_elementos[i+1]): #si la primera pregunta tambien es la segunda entonces eliminamos la segunda
                    del questionState[i+1]
            else:
                if (todos_los_elementos[0] == todos_los_elementos[i]): 
                    del questionState[i]
        #en resumen dejamos las 2 preguntas contestadas recientemente, verificando que no sean las mismas

        print(questionState)

        preguntas_correctas = sum(1 for pregunta in allquestions if pregunta.state == 'Correcta')
        preguntas_erroneas = sum(1 for pregunta in allquestions if pregunta.state == 'Reforzar')
        print("Preguntas correctas:", preguntas_correctas)
        print("Preguntas para reforzar:", preguntas_erroneas)

        # Verificar si se han respondido al menos 3 preguntas erróneas y 3 preguntas para reforzar
        if preguntas_correctas + preguntas_erroneas >= 6:
            # Obtener las últimas 2 respuestas del usuario

            ultimas_respuestas = [pregunta.state for pregunta in questionState[-2:]]
            # Probabilidad de cambiar una pregunta "correcta" a "reforzar" o "nueva"
            if ultimas_respuestas == ['Correcta', 'Correcta'] and random.random() < 0.7:
                # Cambiar una pregunta "correcta" a "reforzar"
                preguntas_erroneas_list = [pregunta for pregunta in allquestions if pregunta.state == 'Reforzar']
                pregunta_seleccionada = random.choice(preguntas_erroneas_list)
                pass
            elif ultimas_respuestas == ['Reforzar', 'Reforzar'] and random.random() < 0.7:
                # Cambiar una pregunta "errónea" a "correcta"
                preguntas_correctas_list = [pregunta for pregunta in allquestions if pregunta.state == 'Correcta']
                pregunta_seleccionada = random.choice(preguntas_correctas_list)
                pass
            else:
                # Indicar que la pregunta debe ser nueva
                return 'nueva'
        else:
            # Indicar que la pregunta debe ser nueva
            return 'nueva'
        #print(pregunta_seleccionada.id)
        return pregunta_seleccionada

class SaveOneAnswer(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    #permission_classes = (IsAuthenticated,)  # Permiso requerido para acceder a la vista
    serializer_class = SaveAnswerSerializer  # Clase serializadora utilizada

    def create(self, request, *args, **kwargs): 
        answer_serializer = self.serializer_class(data = request.data, context={'request': request})
        #print(answer_serializer)
        if answer_serializer.is_valid():
            answer_serializer.save()  # Guardar los datos

            return Response({'message': 'CREATED'}, status=status.HTTP_201_CREATED)  # Devolver una respuesta exitosa
        else:
            answer_serializer.is_valid(raise_exception=True)


class SaveUserQuestion(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SaveUserQuestionState

    def create(self, request, *args, **kwargs): 
        question_user_serializer = self.serializer_class(data=request.data, context={'request': request}) 
        if question_user_serializer.is_valid():
            question_user_serializer.save()  # Guardar los datos
            return Response({'message': 'CREATED'}, status=status.HTTP_201_CREATED)  # Devolver una respuesta exitosa
        else:
            question_user_serializer.is_valid(raise_exception=True)

    
    #def create_or_update(self, request): #definir comportamiento update delete
     #   question_user_serializer = SaveUserQuestionState(data = request.data, context={'request': request})
      #  question_user_serializer.is_valid()
       # question_user_serializer.save()
        #serializer_data = question_user_serializer.data
        
        # Acceder al valor de "exist"
        #exist_value = serializer_data.get('exist',False)
        #print(exist_value)
        ##
    
        #question_user_serializer.is_valid()
        
        #print("state")
        #print(question_user_serializer)

#25-07 para guardar la configuración
class UserEssayConfigCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserEssayConfig.objects.all()
    serializer_class = UserEssayConfigSerializer

    def create(self, request, *args, **kwargs):
        config_Create = self.serializer_class(data = request.data, context={'request': request})
        if config_Create.is_valid():
            config_Create.save()

            return Response({'message':'CREATED'}, status=status.HTTP_201_CREATED)
        else:
            config_Create.is_valid(raise_exception=True)

class UserEssayConfigRetrieveUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserEssayConfig.objects.filter().order_by('pk')  # Obtiene todos los usuarios ordenados por su clave primaria
    serializer_class = UserEssayConfigSerializer


class UserEssayConfigList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    #queryset = UserEssayConfig.objects.prefetch_related('user_Essay_Config_types') este prefetch realiza lo mismo que lo definido en el queryset
    serializer_class = UserEssayConfigSerializer
    #LIST SOLO LOS DE UN USUARIO
    def get_queryset(self): 
        user = self.request.user
        queryset = UserEssayConfig.objects.filter(users_id = user.id)
        return queryset

#27-07

class QuestionListType(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionOneSerializer  # Clase serializadora utilizada, con esta tambien entrega las respuestas
    
    def get_queryset(self): 

        tiposDePreguntas = self.kwargs['tiposDePreguntas'] #
        numeroDePreguntas = self.kwargs['numeroDePreguntas'] #
        UserQuestionState_ids = UserQuestionState.objects.filter(users_id = self.request.user.id).values_list('id', flat=True)
        cantidadPorTipo = 0
        resto = 0
        preguntas = []
        cantidadPorPreguntas = [] 
        print(str(tiposDePreguntas)+'hola')
        print('hola')
        if tiposDePreguntas is not None:

            
            if type(tiposDePreguntas) is not list:
                print(tiposDePreguntas)
                #queryset = Question.objects.filter(type_question_id=tiposDePreguntas).exclude(id__in=UserQuestionState_ids).order_by('?')[:numeroDePreguntas]
            else:
                #identificar cuanto es para cada pregunta si hay mas de una
                cantidadPorTipo = math.floor(numeroDePreguntas/len(tiposDePreguntas))

                for i in range(len(tiposDePreguntas)): #alacenamos la cantidad por pregunta
                        cantidadPorPreguntas.append(cantidadPorTipo)

                #identificar cual de todos los tipos tendra más si la suma no es exacta
                if cantidadPorTipo*len(tiposDePreguntas) != numeroDePreguntas:
                    resto = numeroDePreguntas - cantidadPorTipo*len(tiposDePreguntas)#alacenamos la diferencia para repartirlas entre las preguntas
                    
                    for i in range(resto):#Agregamos de manera aleatoria la diferencia a cada una de las preguntas
                        cantidadPorPreguntas[random.randint(0, len(tiposDePreguntas)-1)] +=1
                    
                    for i in range(len(tiposDePreguntas)):
                        queryset = Question.objects.filter(type_question_id=tiposDePreguntas[i]).exclude(id__in=UserQuestionState_ids).order_by('?')[:cantidadPorPreguntas[i]]
                        preguntas.extend(queryset)
                    
                    return preguntas
                else:
                    queryset = Question.objects.filter(type_question_id__in=tiposDePreguntas).exclude(id__in=UserQuestionState_ids).order_by('?')[:numeroDePreguntas]#si es exacto el numero de pregunta es igual por cada uno
        else:
            raise serializers.ValidationError("Se debe proporcionar los tipos de preguntas")
    
        queryset = Question.objects.order_by('?')[:12]
        return  queryset