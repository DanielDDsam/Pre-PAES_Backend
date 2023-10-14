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
from django.db.models import F
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
        print(serializer)
        if serializer.is_valid():
            serializer.save()  # Guarda los datos del nuevo usuario en la base de datos
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Retorna los datos del usuario registrado en la respuesta con un código de estado 201 (CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Retorna los errores de validación en la respuesta con un código de estado 400 (BAD REQUEST)

class RegisterAdminView(APIView):
    def post(self, request):
        serializer = RegistrationAdminSerializer(data=request.data)  # Serializador utilizado para validar y procesar los datos del formulario
        print('hola')
        if serializer.is_valid():
            serializer.save()  # Guarda los datos del nuevo usuario en la base de datos
            return Response({'message':'admin created', 'data':serializer.data}, status=status.HTTP_201_CREATED)  # Retorna los datos del usuario registrado en la respuesta con un código de estado 201 (CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Retorna los errores de validación en la respuesta con un código de estado 400 (BAD REQUEST)


class LoginView(APIView):
    renderer_classes = [UserRenderer]  # Clase de renderizado utilizada para la vista

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)  # Serializador utilizado para validar y procesar los datos del formulario
        serializer.is_valid(raise_exception=True)  # Valida los datos y lanza una excepción si no son válidos
        email = serializer.data.get('email')  # Obtiene el email del usuario del serializador
        password = serializer.data.get('password')  # Obtiene la contraseña del usuario del serializadorprint(user)
        user = authenticate(email=email, password=password)  # Autentica al usuario utilizando el email y la contraseña
        #user devuelve el objeto user
        if user is not None:
            token = get_tokens_for_user(user)  # Obtiene el token de acceso para el usuario autenticado

            #21-08
            admin = user.is_admin
    
            if admin is True:
                return Response({'token': token, 'msg': 'Inicio de sesión exitoso', 'status': 'ok','user_id':user.id, 'username':user.username, 'is_admin':user.is_admin}, status=status.HTTP_200_OK)  # Retorna el token de acceso en la respuesta con un mensaje de éxito y un código de estado 200 (OK)
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
        print('124'+str(request.data))
        serializer = SendPasswordResetEmailSerializer(data=request.data)  # Serializador utilizado para validar y procesar los datos del formulario
        serializer.is_valid(raise_exception=True)  # Valida los datos y lanza una excepción si no son válidos
        return Response({'msg': 'Link para reiniciar contraseña enviado'}, status=status.HTTP_200_OK)  # Retorna un mensaje de éxito en la respuesta


class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]  # Clase de renderizado utilizada para la vista

    def post(self, request, uid, token, format=None):
        print('134'+str(self.kwargs.get('uid')))
        print('135'+str(self.kwargs.get('uid')))
        serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid,'token':token})  # Serializador utilizado para validar y procesar los datos del formulario
        serializer.is_valid(raise_exception=True)  # Valida los datos y lanza una excepción si no son válidos
        return Response({'msg':'Cambio de contraseña exitoso'}, status=status.HTTP_200_OK)  # Retorna un mensaje de éxito en la respuesta

#################################################################################################################################################################################################

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
    filterset_fields = ['id', 'type_question', 'question', 'subject', 'link_resolution']  # Campos permitidos para filtrar


class QuestionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Question.objects.filter().order_by('pk')  # Consulta para obtener las preguntas ordenadas por clave primaria
    serializer_class = QuestionSerializer  # Clase serializadora utilizada

class QuestionDificultJson(generics.UpdateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = Question.objects.filter().order_by('pk')  # Consulta para obtener las preguntas ordenadas por clave primaria
    serializer_class = QuestionSerializer  # Clase serializadora utilizada

    def get_queryset(self, id):
        return Question.objects.filter(id=id).first()  # Devolver los ensayos personalizados del usuario

    def patch(self, request):

        data = request.data
        instances = []
        for question in data:
            
            questionObject = self.get_queryset(question['id']) 

            if questionObject is not None:
                 print(questionObject.id)
                 questionObject.id = question['id']
                 questionObject.dificult = question['dificult']
                 questionObject.save()
                 instances.append(questionObject)
        serializers = self.serializer_class(instances, many = True)
        return Response(serializers.data)


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

#################################################################################################################################################################################################
class questionAnswers(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionAnswerSerializer
    filter_backends = [DjangoFilterBackend]
    
    def get_queryset(self):
        question_pk = self.kwargs['pk'] #obtenemos la pk de la url
        queryset = Question.objects.filter(id = question_pk)
        return queryset

class oneQuestion(generics.ListAPIView):
    serializer_class = QuestionOneSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated]  # Clases de permisos requeridos para acceder a la vista

    def get_queryset(self):
        user = self.request.user #obtenemos al usuario
        UserQuestionState_ids = UserQuestionState.objects.filter(users_id = user.id).values_list('id', flat=True) #agregar el usuario a que hace referencia 
       
        if UserQuestionState_ids:
            queryset = Question.objects.all().exclude(id__in=UserQuestionState_ids).order_by('?').first() #agregar el else
        else:
            queryset = Question.objects.all().order_by('?').first()
        return queryset

    def list(self, request):
        queryset = self.get_queryset()
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
                queryset = Question.objects.all().exclude(id__in=UserQuestionState_ids).order_by('?').first() #sacamos una pregunta que no este entre las ya contestadas
            else:
                queryset = Question.objects.all().order_by('?').first()#sacamos una pregunta aleatoria
        else:
            queryset = Question.objects.filter(id=pregunta.question_id).first() #si la pregunta no es nueva, es reforzar o correcta la obtenemos 
        return queryset

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = QuestionOneSerializer(queryset) 
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

class SaveOneAnswer(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SaveAnswerSerializer  # Clase serializadora utilizada

    def create(self, request, *args, **kwargs): 
        answer_serializer = self.serializer_class(data = request.data, context={'request': request})

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

#######################################################################################################################################################################################

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
    serializer_class = UserEssayConfigListSerializer
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
        tiposDePreguntas = tiposDePreguntas.replace("[", "")
        tiposDePreguntas = tiposDePreguntas.replace("]", "")
        tipos_de_preguntas_list = tiposDePreguntas.split(',')
        tipos_de_preguntas = list(tipos_de_preguntas_list)

        numeroDePreguntas = int(self.kwargs['numeroDePreguntas']) #
        
        cantidadPorTipo = 0
        resto = 0
        preguntas = []
        cantidadPorPreguntas = [] 
        
        if tipos_de_preguntas is not None:

            if len(tipos_de_preguntas) == 0:
                queryset = Question.objects.filter(type_question_id=tipos_de_preguntas).order_by('?')[:numeroDePreguntas]
            else:
                #identificar cuanto es para cada pregunta si hay mas de una
                cantidadPorTipo = math.floor(numeroDePreguntas/len(tipos_de_preguntas))

                for i in range(len(tipos_de_preguntas)): #alacenamos la cantidad por pregunta
                        cantidadPorPreguntas.append(cantidadPorTipo)

                #identificar cual de todos los tipos tendra más si la suma no es exacta
                if cantidadPorTipo*len(tipos_de_preguntas) != numeroDePreguntas:
                    resto = numeroDePreguntas - cantidadPorTipo*len(tipos_de_preguntas)#alacenamos la diferencia para repartirlas entre las preguntas
                    
                    for i in range(resto):#Agregamos de manera aleatoria la diferencia a cada una de las preguntas
                        cantidadPorPreguntas[random.randint(0, len(tipos_de_preguntas)-1)] +=1
                    
                    for i in range(len(tipos_de_preguntas)):
                        queryset = Question.objects.filter(type_question_id=tipos_de_preguntas[i]).order_by('?')[:cantidadPorPreguntas[i]]
                        preguntas.extend(queryset)
                    
                    return preguntas
                else:
                    for i in range(len(tipos_de_preguntas)):
                        print(numeroDePreguntas/len(tipos_de_preguntas))
                        queryset = Question.objects.filter(type_question_id__in=tipos_de_preguntas[i]).order_by('?')[:(numeroDePreguntas/len(tipos_de_preguntas))]#si es exacto el numero de pregunta es igual por cada uno
                        preguntas.extend(queryset)

                    return preguntas
        else:
            raise serializers.ValidationError("Se debe proporcionar los tipos de preguntas")
    
        return  queryset

class falseCharge(generics.ListAPIView):

    def get(self,request): 
        return Response({'message':'Hola'}, status.HTTP_200_OK)

class bestAverageScore(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserBestEssayScore  # Clase serializadora utilizada
    permission_classes = (IsAuthenticated,)  # Permiso requerido para acceder a la vista

    def get_queryset(self):
        user_pk = self.kwargs['pk']  # Obtener el ID del usuario de los parámetros de la URL
        return CustomEssay.objects.filter(user_id=user_pk).order_by('-created')  # Devolver los ensayos personalizados del usuario
    
    def list(self, request, pk):
        product_serializer = self.get_serializer(self.get_queryset(), many = True)
        bestScore = self.hig_score(product_serializer.data)
        average = self.average_score(product_serializer.data)
        return Response({'bestScore':bestScore,'average':average}, status=status.HTTP_200_OK)
        #return Response({'bestScore':bestScore,'average':average, 'data':data}, status=status.HTTP_200_OK) #este retorna todo junto
    
    def hig_score(self, data):
        score = 0
        dataScore = ''
        for i in range(len(data)):
            if data[i] != []: #evitamos que tome ensayos incompletos
                if(score < data[i]['puntaje']):
                    score = data[i]['puntaje']
                    dataScore = data[i]    
        if (range(len(data)) == 0):
            return 0
        return dataScore
    
    def average_score(self, data):
        average = 0
        validEssayCount = 0
        for i in range(len(data)):
            if data[i] != []: #evitamos que tome ensayos incompletos
                average += int(data[i]['puntaje'])
                validEssayCount+=1

        if (validEssayCount != 0):    
            average = average/validEssayCount  
            return average    
        return 0
    
    def functionEssays(self, queryset):
        data = []
        error = {}
        count = 0
        for i in range(len(queryset)):
            serializer = UserBestEssayScore(queryset[i])
            if len(serializer.data) != 0 & count <= 5: #si el largo es 0 quiere decir que es un ensayo sin respuestas  
                data.append(serializer.data)
                count+=1
            
            if count == 5:
                return data
        
        if count == 0:
            return 0
        return data
    
class CustomEssayMostRecentView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserBestEssayScore  # Clase serializadora utilizada
    
    def get_queryset(self, pk=None):
        user_pk = self.kwargs['pk']  # Obtener el ID del usuario de los parámetros de la URL
        queryset = CustomEssay.objects.filter(user_id=user_pk).order_by('-created')
        return queryset # Devolver los ensayos personalizados del usuario
    
    def list(self, request, pk):
        queryset = self.get_queryset(pk)
        for i in range(len(queryset)):
            serializer = UserBestEssayScore(queryset[i])
            if len(serializer.data) != 0: #si el largo es 0 quiere decir que es un ensayo sin respuestas  
                return Response(serializer.data, status=status.HTTP_200_OK)#retoramos el primero ya que es el más reciente
        return Response({'message':'No hay ensayos realizados por el usuario'}, status=status.HTTP_204_NO_CONTENT)

class CustomEssayMostRecentResumeView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserBestEssayScore  # Clase serializadora utilizada
    
    def get_queryset(self, pk=None):
        user_pk = self.kwargs['pk']  # Obtener el ID del usuario de los parámetros de la URL
        queryset = CustomEssay.objects.filter(user_id=user_pk).order_by('-created')
        return queryset # Devolver los ensayos personalizados del usuario
    
    def list(self, request, pk):
        queryset = self.get_queryset(pk)
        data = []
        count = 0
        for i in range(len(queryset)):
            serializer = UserBestEssayScore(queryset[i])
            if len(serializer.data) != 0 & count <= 5: #si el largo es 0 quiere decir que es un ensayo sin respuestas  
                data.append(serializer.data)
                count+=1
            
            if count == 5:
                return Response(data, status=status.HTTP_200_OK)
        
        if count == 0:
            return Response({'message':'No hay ensayos realizados por el usuario'}, status=status.HTTP_204_NO_CONTENT)
        return Response(data, status=status.HTTP_200_OK)

##################################################################################################################################################################################################################################################

class PrePAESCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PrePAES.objects.filter(is_deleted=False)  # Consulta para obtener los ensayos personalizados que no han sido eliminados
    serializer_class = PrePAESCreateSerializer  # Clase serializadora utilizada

class PrePAESListExistView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PrePAESCreateSerializer  # Clase serializadora utilizada

    def get_queryset(self):
        user = self.request.user
        queryset = PrePAES.objects.filter(user = user).count()
        return queryset # Devolver los ensayos prePAES del usuario

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        if queryset == 0:
            return Response(False)
        return Response(True)

class oneQuestionRulesPrePaes(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionOneSerializer

    def get_queryset(self):
        user = self.request.user#obtenemos el usuario actual 
        data = self.obtener_pregunta(user)#pasamos el usuario para obtener una pregunta
        UserQuestionState_ids = UserQuestionState.objects.filter(users_id = user.id).values_list('question_id', flat=True) #obtenemos los ids de las preguntas contestadas 
        lastPrePAES = PrePAES.objects.filter(user = user).order_by('-created').first()#obtenemos el ultimo prePAES
        prePaesQuestion = PrePAESQuestion.objects.filter(pre_PAES = lastPrePAES).values_list('question_id', flat=True) #obtenemos todas las preguntas de este ultimo prePAES para evitar que obtenga preguntas repetidas en la misma
        print(data)

        if(isinstance(data, UserQuestionState)):
            queryset = Question.objects.filter(id=data.question_id).first() #si es reforzar o correcta la obtenemos 
        else:
            if data['flag'] == 0:
                print('0')
                queryset = Question.objects.filter(dificult = data['dificultad']).order_by('?').first() #retornamos una pregunta inicial que sea de dificultad facil y de cualquier categoria
                print(queryset)
            elif data['flag'] == 1:
                print('1')
                queryset = Question.objects.filter(dificult = data['dificultad'], type_question_id = data['categoria']).exclude(id__in = UserQuestionState_ids).order_by('?').first() #retornamos una pregunta nueva que no sea una de las ya contestadas y respetando la dificultad y categoria
                print('651'+str(queryset))
                if(queryset is None):#si ya no quedan nuevas preguntas per dificultad o categoria, entonces saldra una al alzar repetando lo ultimo y evitan la repetición de alguna de las que ya se encuentran en la fase actual de prePAES
                    queryset = Question.objects.filter(dificult = data['dificultad'], type_question_id = data['categoria']).exclude(id__in = data['prePaesQuestion']).order_by('?').first()
                    if(queryset is None):
                        queryset = Question.objects.filter(dificult = data['dificultad']).exclude(id__in = data['prePaesQuestion']).order_by('?').first()
                print('660'+str(queryset))
            
            
        """print("PREGUNTA:"+str(data['tipo']))
        if data['tipo'] == 'nueva':

            UserQuestionState_ids = UserQuestionState.objects.filter(users_id = user.id).values_list('question_id', flat=True) #obtenemos los ids de las preguntas contestadas 
            print("ids question:"+str(UserQuestionState_ids))

            if UserQuestionState_ids:#vemos si ya contesto alguna pregunta
                queryset = Question.objects.all().exclude(id__in=UserQuestionState_ids).order_by('?').first() #sacamos una pregunta que no este entre las ya contestadas
                print(queryset)
            else:
                queryset = Question.objects.all().order_by('?').first()
                print(queryset)
        else:
            queryset = Question.objects.filter(id=pregunta.question_id).first() #si la pregunta no es nueva, es reforzar o correcta la obtenemos 

        print(queryset.id)"""
        
        return queryset

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        print('queryset:'+str(queryset))

        serializer = self.serializer_class(queryset) 
        print('serializer:'+str(serializer))
        
        self.save_obtain_question(serializer.data)
        serializer.data['answer'] = random.shuffle(serializer.data['answer'])#mezclamos las respuestas
        return Response(serializer.data)
    
    #21-09
    def save_obtain_question(self,questionData):#aqui cristian soy tu yo del pasado, recuerda que aqui va pregunta obtenida, ya que en el metodo pre-paes se puede salir sin problemas, por lo tanto debemos guardarla pasa así saber de donde retornarla 17_08
        user = self.request.user#obtenemos el usuario actual 

        # obtener el id del ultimo ensayo prePAES
        queryset = PrePAES.objects.filter(user = user).order_by('-created').first()
        essaySerializer = PrePAESCreateSerializer(queryset)
    
        #print(queryset)
        #Guardamos la convinación de la fase de prePAES y la pregunta
        print('Question_data: '+str(questionData))
        serializer = PrePAESSaveQuestionSerializer(data={'pre_PAES':essaySerializer.data['id'],'question':questionData['id']}) 
        if(serializer.is_valid()):
            serializer.save()
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
        return serializer.data
    
    def quitarRepeticionesUltimas2Respuestas(self, user):

        create_data = UserQuestionState.objects.filter(users_id = user.id).order_by('-created')[:2] #obtemos las preguntas ordenadas por orden de creación las ultimas primero
        idCreate = []      
        for i in range(len(create_data)):
            idCreate.append(create_data[i].question_id)
        update_data = UserQuestionState.objects.filter(users_id = user.id).exclude(question_id__in=idCreate,created=F('updated')).order_by('-updated')[:2] #obtemos las preguntas ordenadas por orden de modificacion las ultimas primero
 
        todos_los_elementos = list(create_data) + list(update_data) #obtenemos las 2 ultimas creadas y modificadoas
        todos_los_elementos.sort(key=lambda x: max(x.created, x.updated), reverse=True) #mediante max identificamos para cada objeto cual es la fecha mayor y luego el arreglo se ordena
        questionState = []
        questionState.extend(todos_los_elementos[:2])
        
        return questionState
   
    def determinar_dificultad(self, categoria):
        dificultad = PrePAESQuestion.objects.filter(question__type_question=categoria).order_by('-created').values_list('question__dificult').first()#identificamos la ultima pregunta contestada de prePAES de esa categoria
       
        if dificultad is not None:#esto implica que hay una pregunta contestada aun para esa categoria, mas especificamente la más reciente
            return dificultad[0]#por lo que obtenemos la dificultad, en la que se encuentra
        return 'Fácil'#si no ha contestado entonces se retorna Fácil

    def categoriaAleatoria(self):
        categoria = MathType.objects.order_by('?').values_list('id').first()
        return categoria[0]
    
    def determinar_aumentoDeDificultad(self,user, categoria, dificultad):

        prePAESids = PrePAES.objects.filter(user = user).values_list('id')#para que al contar, solo cuente los del usuario actual, no los de los otros
        count = PrePAESQuestion.objects.filter(question__type_question=categoria, question__dificult=dificultad, pre_PAES_id__in=prePAESids).count()#contamos si las preguntas contestadas para esa dificultad y categoria suman 3
        if count % 3 == 0:
            limit = 3 #solo debemos obtener 3
            create_data = UserQuestionState.objects.filter(users_id = user.id, question__type_question=categoria, question__dificult = dificultad).order_by('-created')[:limit]#obtenemos las 
            idCreate = []
            
            for i in range(len(create_data)):
                idCreate.append(create_data[i].question_id)

            update_data = UserQuestionState.objects.filter(users_id = user.id, question__type_question=categoria, question__dificult = dificultad).exclude(question_id__in=idCreate,created=F('updated')).order_by('-updated')[:limit]
            todos_los_elementos = list(create_data) + list(update_data)#combinamos las listas
            todos_los_elementos.sort(key=lambda x: max(x.created, x.updated), reverse=True) #mediante max identificamos para cada objeto cual es la fecha mayor y luego el arreglo se ordena
            todos_los_elementos = todos_los_elementos[:limit]
            
            correcta = 0
            reforzar = 0
            print(categoria)
            print(dificultad)
            print(len(todos_los_elementos[:limit]))
            print(todos_los_elementos)
            print(create_data)
            print(update_data)
            
            for i in range(len(todos_los_elementos[:limit])):
                print('765:'+str(i))
                if(todos_los_elementos[i].state == 'Reforzar'):
                    reforzar+=1
                elif(todos_los_elementos[i].state == 'Correcta'):
                    correcta+=1

            print((correcta/limit)*100)
            print((reforzar/limit)*100)
            if((correcta/limit)*100 >= 60 ):
                return 1 #aumentar dificultad
            elif((reforzar/limit)*100 >= 60 ):
                return 2 #disminuir dificultad
            else:
                return 4 #para indicar que no se aumenta la dificultad y se debe retornar una pregunta aleatoria de la categoria y dificultad establecida
        else:
            return 4
           

    def obtener_pregunta(self, user):

        numberState = UserQuestionState.objects.filter(users_id = user.id).count()
        print('cantidad de estados'+str(numberState))
        if(numberState == 0): #si inicia metodo prePAES entonces la primera preguta sera nueva y facil
            return {"tipo":'nueva',"dificultad":'Fácil',"flag":0}
        else:
            #categoria = 2#de prueba

            categoria = self.categoriaAleatoria()#definimos una categoria de manera aleatoria
            dificultadActual = self.determinar_dificultad(categoria)#determinamos la dificultad actual de la categoria obtenida en base a la ultima pregunta constestada
            aumento = self.determinar_aumentoDeDificultad(user, categoria, dificultadActual) #validar las 3 preguntas contestadas por esa categoria
           
            if aumento == 4:#
                print(aumento)
            else:
                if(aumento == 1):#se aumenta la dificultad
                    print(aumento)
                    if(dificultadActual == 'Fácil'):
                        dificultadActual = 'Media'
                    elif(dificultadActual == 'Media'):
                        dificultadActual = 'Difícil'
                elif(aumento == 2):#se diminuye la dificultad
                    print(aumento)
                    if(dificultadActual == 'Media'):
                        dificultadActual = 'Fácil'
                    elif(dificultadActual == 'Difícil'):
                        dificultadActual = 'Media'
                #en caso de ser 3 la dificultad se mantiene
            print('DIFICULTAD: '+str(dificultadActual))
            lastPrePAES = PrePAES.objects.filter(user = user).order_by('-created').first()#obtenemos el ultimo prePAES
            prePaesQuestion = PrePAESQuestion.objects.filter(pre_PAES = lastPrePAES).values_list('question_id', flat=True) #obtenemos todas las preguntas de este ultimo prePAES para evitar que obtenga preguntas repetidas en la misma
            
            if numberState >= 4:# a partir de 3 preguntas 

                questionState = self.quitarRepeticionesUltimas2Respuestas(user)#quitamos las prosibles preguntas repetidas
                ultimas_respuestas = [pregunta.state for pregunta in questionState] #verificamos en que estado se encuentran las utlimas 2 respuestas 
                preguntas_list = []

                print('814')
                print(ultimas_respuestas)

                # Probabilidad de cambiar una pregunta "correcta" a "reforzar" o "nueva"
                if ultimas_respuestas == ['Correcta', 'Correcta'] and random.random() < 0.7:
                    # Cambiar una pregunta "correcta" a "reforzar"
                    allquestionsObtain = UserQuestionState.objects.filter(users_id = user.id, question__dificult = dificultadActual, question__type_question=categoria).exclude(question_id__in=prePaesQuestion)#quitamos las preguntas de la fase actual de prePAES

                    if (len(allquestionsObtain) != 0):
                        preguntas_list = [pregunta for pregunta in allquestionsObtain if pregunta.state == 'Reforzar']

                    if len(preguntas_list) != 0: #si hay preguntas erroneas obtener alguna de ellas
                        pregunta_seleccionada = random.choice(preguntas_list)
                        print('Correcta correcta entre')
                        return pregunta_seleccionada
                    else:#si no, obtener alguna nueva
                        return {"tipo":"nueva","dificultad":dificultadActual,"categoria":categoria,"flag":1, "prePaesQuestion":prePaesQuestion}
                    
                if ultimas_respuestas == ['Reforzar', 'Reforzar'] and random.random() < 0.7:
                    # Cambiar una pregunta "errónea" a "correcta"
                    allquestionsObtain = UserQuestionState.objects.filter(users_id = user.id, question__dificult = dificultadActual, question__type_question=categoria).exclude(question_id__in=prePaesQuestion)#quitamos las preguntas de la fase actual de prePAES

                    if (len(allquestionsObtain) != 0):
                        preguntas_list = [pregunta for pregunta in allquestionsObtain if pregunta.state == 'Correcta']

                    if len(preguntas_list) != 0:
                        pregunta_seleccionada = random.choice(preguntas_list)
                        print('Reforzar Reforzar entre')
                        return pregunta_seleccionada
                    else:
                        return {"tipo":"nueva","dificultad":dificultadActual,"categoria":categoria,"flag":1, "prePaesQuestion":prePaesQuestion}
                # Indicar que la pregunta debe ser nueva
                return {"tipo":"nueva","dificultad":dificultadActual,"categoria":categoria,"flag":1, "prePaesQuestion":prePaesQuestion}
            else:
                # Indicar que la pregunta debe ser nueva
                return {"tipo":"nueva","dificultad":dificultadActual,"categoria":categoria,"flag":1, "prePaesQuestion":prePaesQuestion}

class UserPrePAESQuestionsListViews(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserPrePAESData  # Clase serializadora utilizada

    def get_queryset(self):
        user = self.request.user  # Obtener el ID del usuario de los parámetros de la URL
        url_solicitada = self.request.path

        if url_solicitada == '/PrePAES_questions_state/':
            queryset = PrePAES.objects.filter(user = user).order_by('-created').first()
        else:
            fase = self.kwargs['fase']
            queryset = PrePAES.objects.filter(user = user, number_phase = fase).order_by('-created').first()
        return queryset # Devolver los ensayos prePAES del usuario

    def list(self, request, **kwargs):#devolvemos la lista de pregunta de la fase actual solo con su estado de correcta o incorrecta
        queryset = self.get_queryset()
        data = []
        indiceDatos = 0
        serializer = UserPrePAESData(queryset)

        if(len(serializer.data['user_PrePAES']) != 0):
                
                data.append(serializer.data)
                for j in range(len(data[indiceDatos]['user_answer'])):#se ocupa eñ estadp ya que úede haber más preguntas que respúestas, ya que puede llegar a obtener una nueva pero no la constesta
                    
                    
                    data[indiceDatos]['user_PrePAES'][j]['answer_state'] = data[indiceDatos]['user_answer'][j]['answer_state']
                    data[indiceDatos]['user_PrePAES'][j]['answer_id'] = data[indiceDatos]['user_answer'][j]['answer_id']

                    #print(data[indiceDatos])
                data[indiceDatos].pop('user_answer')#quitamos el dato para un mejor oden para el frontend
                indiceDatos += 1
        else:
            data.append(serializer.data)
        return Response(data, status=status.HTTP_200_OK)

class AnswerPrePAESView(generics.CreateAPIView): #22-09
    permission_classes = [IsAuthenticated]
    queryset = AnswerPrePAES.objects.filter().order_by('pk')
    serializer_class = SaveAnswerPrePAESSerializer

    def post(self, request): #lo mismo que hicimos en apy.py de users, se usa post ya que es un apiview
        #print(request.data)
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            
            serializer.save()#guarda los datos en la base de datos, si se quiere dar cierta forma consultar este link https://www.django-rest-framework.org/tutorial/1-serialization/
            return Response({'message':'Respuesta guardada correctamente'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) #si no cumple con las validaciones, ya sea que le falta un campo o ya exite lo mostrara

class AnswerPrePAESListView(generics.ListAPIView): #obtiene todas las respuestas de una fase prePAES
    permission_classes = [IsAuthenticated]
    serializer_class = AnswerPrePAESSerializer

    def get_queryset(self):
        question = self.kwargs['question'] # Obtener el ID del usuario de los parámetros de la URL
        queryset = Answer.objects.filter(questions_id = question)
        return queryset # Devolver los ensayos prePAES del usuario
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = []
        for i in range(len(queryset)):
            serializer = AnswerPrePAESSerializer(queryset[i])
            data.append(serializer.data)
        data.append(self.kwargs['question'])
        return Response(data, status=status.HTTP_200_OK)

class oneQuestionDataListView(generics.ListAPIView):
    serializer_class = QuestionOneSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated]  # Clases de permisos requeridos para acceder a la vista

    def get_queryset(self):
        question = self.kwargs['question']
        queryset = Question.objects.filter(id=question)
        return queryset

class stadisticsPrePAESView(generics.ListAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = StadisticsPrePAESSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = UserQuestionState.objects.filter(users = user)
        return queryset
    
    def stateMAX(self, serializer):
        claves = {"Reforzar": {}, "Correcta": {}}
        for data in serializer.data:
            state = data["state"]# Reforzar o Correcta desde los datos de la base de datos
            subject = data["subject"]
            
            if subject not in claves[state]:
                claves[state][subject] = 1
            else:
                claves[state][subject] += 1 #para caba subject suma +1 si aparece

        most_common_subjects = {}
        for state in claves:#iteramos en la claves proporcionado este caso reforzar y Correcta
            most_common_subjects[state] = max(claves[state], key=claves[state].get, default=0)#la funcion max en base a los estados, identifica mediante la obtencion de get cual es el que más se repite em base al elemeto definido, en este caso las claves[state], default da un valor si el iterable esta vacio

        #most_common_subjects = {
         #   state: max(claves[state], key=claves[state].get, default=0) #la funcion max en base a los estados, identifica mediante la obtencion de get cual es el que más se repite em base al elemeto definido, en este caso las claves[state], default da un valor si el iterable esta vacio
          #  for state in claves #iteramos en la claves proporcionado este caso reforzar y Correcta
        #}

        return most_common_subjects
    
    def stateDificult(self, serializer):

        claves = {"probabilidades": {}, "algebra": {}, "geometria": {}, "numeros": {}}

        for data in serializer.data:
            state = data["state"]# Reforzar o Correcta desde los datos de la base de datos
            subject = data["subject"]
            
            if state not in claves[subject]:
                claves[subject][state] = 1
            else:
                claves[subject][state] += 1 #para caba subject suma +1 si aparece

        most_common_state = {
            subject: {state: count for state, count in claves[subject].items()}
            for subject in claves #iteramos en la claves proporcionado este caso reforzar y Correcta
        }

        return most_common_state

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        most_common_subjects = self.stateMAX(serializer)
        most_common_state = self.stateDificult(serializer)
        dificult_subjects = {}
        j = 0
        print('data :'+str(most_common_state))
        for i in most_common_state:
            
            reforzar = most_common_state[i].get('Reforzar')
            correcta = most_common_state[i].get('Correcta')
            keys = list(most_common_state.keys())
            print(keys[j])
            print(j)

            if reforzar is None:
                dificult_subjects[keys[j]] = 'Dificil'
            elif correcta is None:
                dificult_subjects[keys[j]] = 'Facil'
            else:
                if reforzar > correcta:
                    dificult_subjects[keys[j]] = 'Facil'
                if reforzar < correcta:
                    dificult_subjects[keys[j]] = 'Dificil'
                if reforzar == correcta:
                    dificult_subjects[keys[j]] = 'Intermedio'        
            
            j+=1
               
        data = []
        data.append(most_common_subjects)
        data.append(most_common_state)
        data.append(dificult_subjects)

        return Response(data, status=status.HTTP_200_OK)
    
