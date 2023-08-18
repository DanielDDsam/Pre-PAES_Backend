from api.models import *
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail, get_connection
from backend.settings import EMAIL_HOST_USER

generic_fields = ['created', 'updated', 'is_deleted']


#serializadores para class user


# Serializador para el modelo Users
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        exclude = [*generic_fields, 'is_admin']

# Serializador para el login del usuario
class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = Users
        fields = ['email', 'password','username']

# Serializador para el perfil del usuario
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email', 'username']


# Serializador para el registro del usuario, compara las contraseñas para verificar que coincidan
class RegistrationSerializer(serializers.ModelSerializer):
    # Atributos requeridos para el registro del usuario
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    username = serializers.CharField(max_length=255)

    class Meta:
        model = Users
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # Método para guardar el usuario en la base de datos
    def save(self):
        user = Users(email=self.validated_data['email'], username=self.validated_data['username'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        # Verificar que las contraseñas coincidan
        if password != password2:
            raise serializers.ValidationError({'password': 'Las contraseñas deben coincidir.'})
        # Establecer la contraseña del usuario y guardarlo
        user.set_password(password)
        user.save()
        return user


# Serializador para cambiar la contraseña del usuario
class PasswordChangeSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)

    class Meta:
        fields = ['password', 'password2']

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get('user')

        # Verificar que las contraseñas coincidan
        if password != password2:
            raise serializers.ValidationError("Las contraseñas no coinciden")

        # Cambiar la contraseña del usuario
        if user.check_password(password):
            raise serializers.ValidationError("La nueva contraseña debe ser diferente a la contraseña actual")
        user.set_password(password)
        user.save()
        return attrs

class PasswordChangeProfileSerializer(serializers.Serializer):
    actualPassword = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)
    password = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)

    class Meta:
        fields = ['actualPassword','password', 'password2']

    def validate(self, attrs):
        actualPassword = attrs.get('actualPassword')
        password = attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get('user')

        # Verificar que las contraseñas coincidan
        if password != password2:
            raise serializers.ValidationError("Las contraseñas no coinciden")

        # Cambiar la contraseña del usuario
        if user.check_password(password):
            raise serializers.ValidationError("La nueva contraseña debe ser diferente a la contraseña actual")
        
        if user.check_password(actualPassword):
            user.set_password(password)
            user.save()
            return attrs
        else:
            raise serializers.ValidationError("La contraseña actual no es valida")

# Serializador para enviar un correo de restablecimiento de contraseña
class SendPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)

    def validate(self, attrs):
        email = attrs.get('email')

        # Verificar si el usuario existe en la base de datos
        if Users.objects.filter(email=email).exists():
            user = Users.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            link = 'http://localhost:3000/api/user/reset/'+uid+'/'+token

            # Enviar el correo electrónico de restablecimiento de contraseña
            subject = 'Reinicia tu contraseña'
            message = f'Presiona el siguiente link para reiniciar tu contraseña: {link}/'
            from_email = EMAIL_HOST_USER
            recipient_list = [email]
            connection = get_connection()
            connection.open()
            send_mail(subject, message, from_email, recipient_list)
            connection.close()
            return attrs
        else:
            raise serializers.ValidationError('No eres un usuario registrado')

# Serializador para restablecer la contraseña del usuario
class UserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)

    class Meta:
        fields = ['password', 'password2']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            password2 = attrs.get('password2')
            uid = self.context.get('uid')
            token = self.context.get('token')

            # Verificar que las contraseñas coincidan
            if password != password2:
                raise serializers.ValidationError("Las contraseñas no coinciden")

            # Decodificar el UID y obtener el usuario correspondiente
            id = smart_str(urlsafe_base64_decode(uid))
            user = Users.objects.get(id=id)

            # Verificar que el token sea válido
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise serializers.ValidationError('El token no es válido o ha expirado')

            # Cambiar la contraseña del usuario
            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user, token)
            raise serializers.ValidationError('El token no es válido o ha expirado')


# Serializador para Answer
class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        exclude = [*generic_fields, 'questions', 'users', 'essay']


# Serializador para crear Answer
class AnswerCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        exclude = [*generic_fields, 'users']


# Serializador para Question
class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        exclude = [*generic_fields, 'type_question']


# Serializador para crear Question
class QuestionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        exclude = [*generic_fields]


# Serializador para Essay
class EssaySerializer(serializers.ModelSerializer):

    class Meta:
        model = MathType
        exclude = [*generic_fields]


# Serializador para AnswerEssayUser
class AnswerEssayUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerEssayUser
        fields = ['essays', 'score', 'answers']


# Serializador para mostrar las respuestas y sus preguntas, junto con la ID del tipo de ensayo
class QuestionsAlternativeAllSerializer(QuestionSerializer):
    answer = AnswerSerializer(many=True, read_only=True)

    def to_representation(self, instance: Question):
        # Llama al método de representación de la superclase para obtener la representación básica de la pregunta
        data = super().to_representation(instance)
        # Obtiene el tipo de ensayo al que pertenece la pregunta
        type_question = instance.type_question
        # Agrega la ID del ensayo a los datos de la pregunta
        data['type_question'] = type_question.id
        return data


# Serializador para mostrar el ensayo y todas sus preguntas y respuestas
class EssayQuestionsAlternativeAllSerializer(EssaySerializer):
    question = QuestionsAlternativeAllSerializer(many=True, read_only=True)


# Serializador para guardar las respuestas de un ensayo creado para un usuario
class SaveAnswersSerializer(serializers.Serializer):
    answer_ids = serializers.ListSerializer(child=serializers.IntegerField())
    user_essay_id = serializers.IntegerField()
    time_essay = serializers.CharField()

    def validate(self, data):
        answer_ids = data.get('answer_ids')
        user_essay_id = data.get('user_essay_id')
        time_essay = data.get('time_essay')

        # Obtener el ensayo personalizado del usuario
        # user_essay = get_object_or_404(CustomEssay, pk=user_essay_id)
        # Filtrar las respuestas según los IDs proporcionados y verificar si pertenecen al ensayo del usuario
        # answers = Answer.objects.filter(id__in=answer_ids, questions__essays__custom_essay=user_essay)

        # # Comprobar si el número de IDs de respuesta coincide con el número de respuestas válidas
        # if len(answer_ids) != len(answers):
        #     raise serializers.ValidationError('Respuestas no válidas.')

        return data

    def create(self, validated_data):
        answer_ids = validated_data.get('answer_ids')
        user_essay_id = validated_data.get('user_essay_id')
        time_essay = validated_data.get('time_essay')

        # Obtener el ensayo personalizado del usuario
        user_essay = get_object_or_404(CustomEssay, pk=user_essay_id)
        user = self.context['request'].user
        essay_answers = []

        # Crear objetos AnswerEssayUser para cada respuesta seleccionada
        for answer_id in answer_ids:
            answer = get_object_or_404(Answer, pk=answer_id)

            # Verificar si ya existe una respuesta para la combinación de UserEssay y Answer
            if AnswerEssayUser.objects.filter(answers=answer, essays=user_essay, users=user).exists():
                raise serializers.ValidationError('Ya existe una respuesta para esta combinación de UserEssay y Answer.')

            # Crear el objeto AnswerEssayUser
            essay_answer = AnswerEssayUser.objects.create(answers=answer, essays=user_essay, users=user,
                                                          score=answer.right, time_essay=time_essay)
            essay_answers.append(essay_answer)

        return essay_answers

class SaveAnswerSerializer(serializers.Serializer):
    answer_id = serializers.IntegerField()
    user_essay_id = serializers.IntegerField()
    time_essay = serializers.CharField()

    def validate(self, data):
        answer_id = data.get('answer_id')
        user_essay_id = data.get('user_essay_id')
        time_essay = data.get('time_essay')

        # Obtener el ensayo personalizado del usuario
        # user_essay = get_object_or_404(CustomEssay, pk=user_essay_id)
        # Filtrar las respuestas según los IDs proporcionados y verificar si pertenecen al ensayo del usuario
        # answers = Answer.objects.filter(id__in=answer_ids, questions__essays__custom_essay=user_essay)

        # # Comprobar si el número de IDs de respuesta coincide con el número de respuestas válidas
        # if len(answer_ids) != len(answers):
        #     raise serializers.ValidationError('Respuestas no válidas.')

        return data

    def create(self, validated_data):
        answer_id = validated_data.get('answer_id')
        user_essay_id = validated_data.get('user_essay_id')
        time_essay = validated_data.get('time_essay')

        print(answer_id)
        # Obtener el ensayo personalizado del usuario
        user_essay = get_object_or_404(CustomEssay, pk=user_essay_id)
        user = self.context['request'].user


        # Crear objetos AnswerEssayUser para la respuesta seleccionada
        answer = get_object_or_404(Answer, pk=answer_id)

        if AnswerEssayUser.objects.filter(answers=answer, essays=user_essay, users=user).exists():
                raise serializers.ValidationError('Ya existe una respuesta para esta combinación de UserEssay y Answer.')
        
        essay_answer = AnswerEssayUser.objects.create(answers=answer, essays=user_essay, users=user,
                                                          score=answer.right, time_essay=time_essay)


        return essay_answer

# Serializador para mostrar el historial de ensayos de un usuario
class UserEssayHistorySerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()  # Campo para obtener la fecha de creación del ensayo

    class Meta:
        model = CustomEssay
        fields = ['id','name', 'is_custom', 'date','current_questions']  # Campos a incluir en la representación del ensayo

    def get_date(self, instance):
        return instance.created.date()  # Método para obtener la fecha de creación del ensayo

    def get_score(self, instance):
        if instance.current_questions == 0:
            return 0
        if instance.current_questions is None:
            return 0
        answers = AnswerEssayUser.objects.filter(essays=instance)
        right = answers.filter(score=1).count()
        score = 100 + (900 / instance.current_questions) * right  # Cálculo del puntaje basado en las respuestas correctas
        return round(score)

    def get_time(self, instance):
        answer_essay_user = instance.answers_essay_user.first()
        if answer_essay_user:
            return answer_essay_user.time_essay
        else:
            return None  # Método para obtener el tiempo empleado en el ensayo

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['time_essay'] = self.get_time(instance)  # Incluir el tiempo empleado en el ensayo en la representación
        data['puntaje'] = self.get_score(instance) 
        print(data) # Incluir el puntaje obtenido en la representación
        # Verificar si hay registros en AnswerEssayUser para el CustomEssay actual
        has_answer_essay_user = AnswerEssayUser.objects.filter(essays=instance).exists()
        if not has_answer_essay_user:
            # No mostrar el CustomEssay si no hay registros en AnswerEssayUser
            return None

        return data

class TypesEssaySerializer(serializers.ModelSerializer):
    class Meta:
        model = TypesEssayCustom
        fields = ['id']  # Selecciona solo el campo 'id' del modelo EssayAnswer

class CustomEssaySerializer(serializers.ModelSerializer):
    type_math_ids = serializers.ListField(write_only=True)  # Campo de lista solo para escritura

    # Se utiliza el serializador EssayAnswerSerializer para el campo 'essay_custom'
    essay_custom = TypesEssaySerializer(many=True, read_only=True)#10-08-2023 ver esto y verificar si no es necesario

    class Meta:
        model = CustomEssay
        fields = ('id', 'is_custom', 'name', 'type_math_ids', 'essay_custom', 'user','current_questions')

    def validate(self, attrs):
        type_math_ids = attrs.get('type_math_ids', [])
        user = attrs.get('user')

        if user is None:
            raise serializers.ValidationError("Se debe proporcionar la id del usuario.")  # Validar que se proporcione la ID del usuario

        # Verificar que los IDs de los tipos de ensayos de matematicas que existan en typemath
        for type_math_id in type_math_ids:
            try:
                essay = MathType.objects.get(id=type_math_id)
            except MathType.DoesNotExist:
                raise serializers.ValidationError(f"La ID del tipo de matematica {type_math_id} no existe.")  # Validar que los IDs de los tipos de matematicas existan en el modelo TypeMath

        return attrs

    def create(self, validated_data):
        type_math_ids = validated_data.pop('type_math_ids', [])
        custom_essay = CustomEssay.objects.create(**validated_data)  # Crear una instancia de CustomEssay con los datos validados

        # Crear objetos EssayAnswer asociados al CustomEssay creado
        for type_math_id in type_math_ids:
            type_essays = MathType.objects.get(id=type_math_id)
            TypesEssayCustom.objects.create(type_essays=type_essays, custom_essay=custom_essay)

        return custom_essay


class CustomEssayQuestionSerializer(serializers.ModelSerializer):
    # Campo 'questions' que es una lista de claves primarias relacionadas con el modelo Question
    questions = serializers.ListField(child=serializers.PrimaryKeyRelatedField(queryset=Question.objects.filter(is_deleted=False)))

    class Meta:
        model = CustomEssayQuestion
        fields = ['custom_essay', 'questions']  # Campos del serializador

    def validate(self, attrs):
        custom_essay = attrs.get('custom_essay')  # Obtener el ID del ensayo personalizado
        questions = attrs.get('questions')  # Obtener las claves primarias de las preguntas seleccionadas

        try:
            custom_essay_obj = CustomEssay.objects.get(id=custom_essay)  # Obtener el objeto CustomEssay correspondiente al ID
        except CustomEssay.DoesNotExist:
            raise serializers.ValidationError('El ensayo personalizado no existe.')  # Validar que el ensayo personalizado exista

        # Verificar que las preguntas existan en los ensayos seleccionados del ensayo personalizado
        essay_ids = custom_essay_obj.essays.values_list('id', flat=True)  # Obtener los IDs de los ensayos predefinidos seleccionados
        for question_id in questions:
            try:
                question_obj = Question.objects.get(id=question_id)  # Obtener el objeto Question correspondiente a la clave primaria
                if question_obj.essays.filter(id__in=essay_ids).exists():
                    continue  # Si la pregunta existe en los ensayos predefinidos seleccionados, continuar con la siguiente pregunta
                else:
                    raise serializers.ValidationError('Una o más preguntas no existen en los ensayos predefinidos seleccionados del ensayo personalizado.')  # Validar que las preguntas existan en los ensayos predefinidos seleccionados
            except Question.DoesNotExist:
                raise serializers.ValidationError('Una o más preguntas no existen en los ensayos predefinidos seleccionados del ensayo personalizado.')  # Validar que las preguntas existan en los ensayos predefinidos seleccionados

        return attrs



class CustomEssayResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomEssay
        exclude = ('updated', 'is_deleted')

#metodo para obtener los parametros de las respuestas
    def get_answers(self,question):
        answers = []
        for answer in Answer.objects.filter(questions=question):
            answer_dict = {
                'label':answer.label,
                'right':answer.right,
                'answer_id':answer.id
            }
            answers.append(answer_dict)
        return answers

#metodo para obtener las preguntas y linkear las alternativas
    def get_question(self,answer):
        questions = []
        for question in Question.objects.filter(answer__in=answer):
            question_dict = {
                'question': question.question,
                'link': question.link_resolution,
                'answer': self.get_answers(question.id)
            }
            questions.append(question_dict)
        return questions


    def get_score(self, instance):
        if instance.current_questions == 0:
            return 0
        if instance.current_questions is None:
            return 0
        answers = AnswerEssayUser.objects.filter(essays=instance)
        right = answers.filter(score=1).count()
        score = 100 + (900 / instance.current_questions) * right  # Cálculo del puntaje basado en las respuestas correctas
        return round(score)


    def to_representation(self, instance: CustomEssay):
        data = super().to_representation(instance)
        answers_list=[]
        answers = instance.answers_essay_user.filter(essays=instance)
        for answer in answers:
            answers_list.append(answer.answers.id)
        print(answers_list)
        data['question'] = self.get_question(answers_list) #trae todos los datos a partir de las respuestas que se respondieron para un ensayo en especifico
        data['answered'] = answers_list #entrega el listado con las id de las respuestas para el ensayo
        data['score'] = self.get_score(instance)
        return data

####################################

class AnswerSerializerSpecific(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['id', 'label', 'right']

class QuestionSerializerSpecific(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['answer']

#serializador que retornara las respuestas de las preguntas
class QuestionAnswerSerializer(QuestionSerializerSpecific): #Heredar de QuestionSerializer

        answer = AnswerSerializerSpecific(many=True, read_only=True) #instancia de las respuestas
        #debe llamare igual que el related-name de la realcion 
        #def to_representation(self, instance: Question):
          #  data = super().to_representation(instance)#usara el metodo to respresentation de la clase QuestionSerializer para la instacia del modelo questions
         #   essay = instance.essays
           # data['essay'] = essay.id
            #return data

class QuestionOneSerializer(QuestionSerializer):
    answer = AnswerSerializerSpecific(many=True, read_only=True)

class UserQuestionStateSerializer(serializers.ModelSerializer): #18-07 este solo se usara para mostar los datos de esta tabla, ya que como tiene elementos de otras, lo idel es usar el de abajo para crearlos
    class Meta:
        model = UserQuestionState
        fields = ['state','question_id','user_id']

class SaveUserQuestionState(serializers.Serializer): #18-07
    answer_id = serializers.IntegerField()

    def validate(self, data):
        answer_id = data.get('answer_id')

        # Obtener el ensayo personalizado del usuario
        # user_essay = get_object_or_404(CustomEssay, pk=user_essay_id)
        # Filtrar las respuestas según los IDs proporcionados y verificar si pertenecen al ensayo del usuario
        # answers = Answer.objects.filter(id__in=answer_ids, questions__essays__custom_essay=user_essay)

        # # Comprobar si el número de IDs de respuesta coincide con el número de respuestas válidas
        # if len(answer_ids) != len(answers):
        #     raise serializers.ValidationError('Respuestas no válidas.')

        return data
    
    def validarExistencia(self, question, user): #todo esto porque tiene daots de otras tablas, verificar si se puede hacer de otra manera
        if UserQuestionState.objects.filter(question=question, users=user).exists():
            return True
        return False

    def create(self, validated_data):
        answer_id = validated_data.get('answer_id') #obtenemos el id de la respuesta
   
        # Obtener la respuesta que contesto el usuario, para luego obtener la pregunta
        answer = get_object_or_404(Answer, pk=answer_id)
        question = get_object_or_404(Question, pk=answer.questions_id)

        #obtenemos el usuario
        user = self.context['request'].user

        
        if self.validarExistencia(question, user) == True:
            #instance = UserQuestionState.objects.filter(question=question, users=user)#obtenemos la instancia
            instance = get_object_or_404(UserQuestionState, question=question, users=user) #si existe obtenemos la instancia
            print(instance)
            if answer.right == 0:
                #instance.update(question=question, users=user,state='Reforzar')
                #return instance
                instance.state = 'Reforzar'
                instance.save()#guardamos el cambio, esto permite modificar el campo update
            else:
                #instance.update(question=question, users=user,state='Correcta')
                #return instance
                instance.state = 'Correcta'
                instance.save()#guardamos el cambio, esto permite modificar el campo update
        else:#si no existe creamos una instancia
            if answer.right == 0:
                instance = UserQuestionState.objects.create(question=question, users=user,state='Reforzar')
            else:
                instance = UserQuestionState.objects.create(question=question, users=user,state='Correcta')
        
        
        return instance

####################################
#25-07

class UserEssayConfigTypesSerializer(serializers.ModelSerializer):
    math_type_id = serializers.IntegerField(source='essay_types.id')#el nombre que tiene el campo en el modelo y que se relaciona con la tabla mathType
    math_type_type = serializers.CharField(source='essay_types.type')

    class Meta:
        model = UserEssayConfigTypes
        fields = ['math_type_id','math_type_type']

class UserEssayConfigListSerializer(serializers.ModelSerializer):
    #type_math_ids = serializers.ListField(write_only=True)  # Campo de lista solo para escritura
    user_Essay_Config_types_all  = UserEssayConfigTypesSerializer(many=True, read_only=True, source='user_Essay_Config_types')
    #debe llamare igual que el related-name de la realcion 
    #essays = UserEssayConfigTypesSerializer(many = True, read_only = True) #indicamos el mucho de la relación, en este caso el tipo de ensayo
    
    class Meta:
        model = UserEssayConfig
        #fields = ['users', 'essay_ids', 'questionNumber']
        exclude = [*generic_fields,'users','essays_types']

class UserEssayConfigSerializer(serializers.ModelSerializer):
    type_math_ids = serializers.ListField(write_only=True)  # Campo de lista solo para escritura
    #user_Essay_Config_types_all  = UserEssayConfigTypesSerializer(many=True, read_only=True, source='user_Essay_Config_types')
    #debe llamare igual que el related-name de la realcion 
    #essays = UserEssayConfigTypesSerializer(many = True, read_only = True) #indicamos el mucho de la relación, en este caso el tipo de ensayo
    
    class Meta:
        model = UserEssayConfig
        #fields = ['users', 'essay_ids', 'questionNumber']
        exclude = [*generic_fields]
    
    def validate(self, attrs):
        
        user = self.context['request'].user
        number_user_config = UserEssayConfig.objects.filter(users=user).count()

        if number_user_config > 40:
             raise serializers.ValidationError({'message': 'Actualmente, solo puedes almacenar hasta 4 configuraciones.'})
        
        return attrs
    
    def create(self, validated_data):
        user = self.context['request'].user
        print(user)
        type_math_ids = validated_data.pop('type_math_ids', [])#sacamos los id de los tipos de ensayos de los datos validados
        print(validated_data)
        user_config = UserEssayConfig.objects.create(**validated_data)  # Crear una instancia de la configuración con los datos validados

        # Crear objetos EssayAnswer asociados al CustomEssay creado
        for type_math_id in type_math_ids:
            essay = MathType.objects.get(id=type_math_id)
            UserEssayConfigTypes.objects.create(users_essasy_config = user_config,essay_types=essay)

        return user_config
    
    def update(self, instance, validated_data):
        type_math_ids = validated_data.pop('type_math_ids', [])  # sacamos los id de los tipos de ensayos de los datos validados

        updateConfig = super().update(instance, validated_data)
        #updateConfig.essays.exclude(id__in=essay_ids).delete()

        # Crear o actualizar objetos UserEssayConfigTypes asociados al UserEssayConfig
        print(updateConfig)

        if type_math_ids: #eliminamos sus configuraciones anteriores
            UserEssayConfigTypes.objects.filter(users_essasy_config=updateConfig).delete()#obtenemos primeros las instancias y las eliminamos

        for type_math_id in type_math_ids:
            essay = MathType.objects.get(id=type_math_id)
            UserEssayConfigTypes.objects.update_or_create(users_essasy_config=updateConfig, essay_types=essay)
            

        updateConfig.save()
        return updateConfig

class UserBestEssayScore(serializers.ModelSerializer):

    date = serializers.SerializerMethodField()  # Campo para obtener la fecha de creación del ensayo

    class Meta:
        model = CustomEssay
        fields = ['id','name', 'is_custom', 'date','current_questions']  # Campos a incluir en la representación del ensayo

    def get_date(self, instance):
        return instance.created.date()  # Método para obtener la fecha de creación del ensayo

    def get_best_score(self, instance):
        if instance.current_questions == 0:
            return 0
        if instance.current_questions is None:
            return 0
        answers = AnswerEssayUser.objects.filter(essays=instance)
        right = answers.filter(score=1).count()
        score = 100 + (900 / instance.current_questions) * right  # Cálculo del puntaje basado en las respuestas correctas
        return round(score)

    def get_time(self, instance):
        answer_essay_user = instance.answers_essay_user.first()
        if answer_essay_user:
            return answer_essay_user.time_essay
        else:
            return None  # Método para obtener el tiempo empleado en el ensayo

    def to_representation(self, instance : CustomEssay):
        
        data = super().to_representation(instance) #obtenemos la data cuando se llamara al serializador del llamado al serializador
        data['time_essay'] = self.get_time(instance)  # Incluir el tiempo empleado en el ensayo en la representación
        data['puntaje'] = self.get_best_score(instance)  # Incluir el puntaje obtenido en la representación
        
        # Verificar si hay registros en AnswerEssayUser para el CustomEssay actual
        has_answer_essay_user = AnswerEssayUser.objects.filter(essays=instance).exists()
        if not has_answer_essay_user:
            
            #se retorna [ ] ya que None deja un error al intentar evaluarlo mediante if en la view
            return []

        
        return data
