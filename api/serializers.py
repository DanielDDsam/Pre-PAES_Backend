from api.models import *
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail, get_connection
from backend.settings import EMAIL_HOST_USER
from django.utils import timezone

generic_fields = ['created', 'updated', 'is_deleted']


#serializadores para class user


# Serializador para el modelo Users
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        exclude = ['created', 'updated', 'is_admin', 'password']

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
        fields = ['email', 'username', 'avatar']


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

class RegistrationAdminSerializer(serializers.ModelSerializer):
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
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Las contraseñas deben coincidir.'})

        user = Users.objects.create_superuser(email=self.validated_data['email'], username=self.validated_data['username'], password=self.validated_data['password'])
        # Verificar que las contraseñas coincidan
        
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
        print('148'+str(email))
        # Verificar si el usuario existe en la base de datos
        if Users.objects.filter(email=email).exists():
            user = Users.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            link = 'https://prepaesbeta.netlify.app/Reset/Password/'+str(uid)+'/'+str(token)

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
            print('id lb 191:'+str(uid))
            # Decodificar el UID y obtener el usuario correspondiente
            id = smart_str(urlsafe_base64_decode(uid))
            user = Users.objects.get(id=id)
            print('id lb 191:'+str(id))

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
        exclude = ['created', 'updated', 'type_question']


# Serializador para crear Question
class QuestionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        exclude = [*generic_fields]

    #06-10 cambiar para que identifique el nombre y no por id
    def create(self, validated_data):
        questionData = validated_data.get('question')
        subjectData = validated_data.get('subject')
        link_resolutionData = validated_data.get('link_resolution')

        # Obtener el ensayo personalizado del usuario

        if subjectData == 'algebra':
            type_question = get_object_or_404(MathType, type='algebra')
        elif subjectData == 'numeros':
            type_question = get_object_or_404(MathType, type='numeros')
        elif subjectData == 'probabilidades':
            type_question = get_object_or_404(MathType, type='probabilidades')
        elif subjectData == 'geometria':
            type_question = get_object_or_404(MathType, type='geometria')

        if Question.objects.filter(question = questionData).exists():#verifica que no haya otra pregunta con el mismo enunciado
                raise serializers.ValidationError('Ya existe una pregunta con este enunciado')

            # Crear el objeto AnswerEssayUser
        question = Question.objects.create(subject=subjectData, question=questionData, link_resolution=link_resolutionData,type_question=type_question)
        return question
    


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
    
    def validateAchievements(self, maxpoint, answer_ids, user, user_essay):

        achievemetFirst = Achievement.objects.filter(name = 'Mi primer ensayo').first()
        userAchievementFirstEssay = UserAchievement.objects.filter(user=user, achievement=achievemetFirst).first()

        achievementMax = Achievement.objects.filter(name = 'Excelencia en Matemáticas').first()
        userAchievementMax = UserAchievement.objects.filter(user=user, achievement=achievementMax).first()
        print(userAchievementFirstEssay)
        print(userAchievementMax)
        print(maxpoint)
        print(len(answer_ids))
        if(userAchievementFirstEssay is None):
            UserAchievement.objects.create(user=user, achievement=achievemetFirst)#relacionado al primer logro que es por realizar un método ensayo

        print('maxpoint' +str(maxpoint)) 
        print(user_essay.current_questions) 
        if (userAchievementMax is None and maxpoint == user_essay.current_questions):
            UserAchievement.objects.create(user=user, achievement=achievementMax)#relacionado al primer logro que es por realizar un método ensayo


    def create(self, validated_data):
        answer_ids = validated_data.get('answer_ids')
        user_essay_id = validated_data.get('user_essay_id')
        time_essay = validated_data.get('time_essay')

        # Obtener el ensayo personalizado del usuario
        user_essay = get_object_or_404(CustomEssay, pk=user_essay_id)
        user = self.context['request'].user
        essay_answers = []
        maxpoint = 0
        # Crear objetos AnswerEssayUser para cada respuesta seleccionada
        for answer_id in answer_ids:
            answer = get_object_or_404(Answer, pk=answer_id)

            # Verificar si ya existe una respuesta para la combinación de UserEssay y Answer
            if AnswerEssayUser.objects.filter(answers=answer, essays=user_essay, users=user).exists():
                raise serializers.ValidationError('Ya existe una respuesta para esta combinación de UserEssay y Answer.')

            # Crear el objeto AnswerEssayUser
            essay_answer = AnswerEssayUser.objects.create(answers=answer, essays=user_essay, users=user,
                                                          score=answer.right, time_essay=time_essay)
            
            if (answer.right == 1):
                maxpoint+=1

            essay_answers.append(essay_answer)

        self.validateAchievements(maxpoint,answer_ids,user, user_essay)
        
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
        data['puntaje'] = self.get_score(instance) # Incluir el puntaje obtenido en la representación
        #print(data) 
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
        fields = ('id', 'is_custom', 'name', 'type_math_ids', 'essay_custom', 'user','current_questions','prePaes')

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

        count = CustomEssay.objects.filter(is_custom = True, user = self.context['request'].user).count()
        achievemet = Achievement.objects.filter(name = 'Creador de Ensayos').first()
        achievmentFirstCustom = UserAchievement.objects.filter(user=self.context['request'].user, achievement=achievemet).first() 
        if (count >= 1 and achievmentFirstCustom is None):
            UserAchievement.objects.create(user=self.context['request'].user, achievement=achievemet)


        return custom_essay


class CustomEssayQuestionSerializer(serializers.Serializer): #modificado el 12-09 para provar la obtencion de pregunta de prepaes
    # Campo 'questions' que es una lista de claves primarias relacionadas con el modelo Question

    question_ids = serializers.ListSerializer(child=serializers.IntegerField())
    user_essay_id = serializers.IntegerField()
    
    def create(self, validated_data):
        question_ids = validated_data.get('question_ids')
        user_essay_id = validated_data.get('user_essay_id')

        # Obtener el ensayo personalizado del usuario
        user_essay = get_object_or_404(CustomEssay, pk=user_essay_id)
        user = self.context['request'].user
        essay_answers = []
        maxpoint = 0
        # Crear objetos AnswerEssayUser para cada respuesta seleccionada
        for question_id in question_ids:
            question = get_object_or_404(Question, pk=question_id)

            # Verificar si ya existe una respuesta para la combinación de UserEssay y Answer
            if CustomEssayQuestion.objects.filter(question=question, custom_essay=user_essay).exists():
                raise serializers.ValidationError('Ya existe una respuesta para esta combinación de ensayo personalizado y pregunta.')

            # Crear el objeto AnswerEssayUser
            essay_question = CustomEssayQuestion.objects.create(question=question, custom_essay=user_essay)
            
        return essay_question


    """def validate(self, attrs):
        custom_essay = attrs.get('custom_essay')  # Obtener el ID del ensayo personalizado
        questions = attrs.get('questions')  # Obtener las claves primarias de las preguntas seleccionadas
        print(custom_essay.id)
        try:
            custom_essay_obj = CustomEssay.objects.get(id=custom_essay.id)  # Obtener el objeto CustomEssay correspondiente al ID
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

        return attrs"""



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
    def get_question(self, instance):
        questions = []
        
        data = CustomEssayQuestion.objects.filter(custom_essay = instance).values_list('question_id')
        print('data id question : '+str(data))

        ordered_ids = [id for id, in data]
        questionsh = Question.objects.filter(id__in=data)
        question_data_sorted = sorted(questionsh, key=lambda x: ordered_ids.index(x.id))

        print(question_data_sorted)

        for question in question_data_sorted:
            question_dict = {
                'id':question.id,
                'question': question.question,
                'link': question.link_resolution,
                'answer': self.get_answers(question.id)
            }
            print(question_dict['id'])
            questions.append(question_dict)
     
        return questions
    
    def order_answers(self, answers, questions):

        dataOrder = []
        count = 0
        print(answers)

        for i in questions:
            print(i['id'])
            count = 0
            for j in i['answer']:
                print('answer id :'+str(j['answer_id']))
                #print('answers :'+str(answers))
                if j['answer_id'] in answers:
                    dataOrder.append(j['answer_id'])
                    
                    break
                else:
            
                    count+=1
                    if count == 4:
                        dataOrder.append('')
                        
                        break
        print(dataOrder)
        return dataOrder


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
      
        data['question'] = self.get_question(instance) #trae todos los datos a partir de las respuestas que se respondieron para un ensayo en especifico
        
        
        data['answered'] = self.order_answers(answers_list, data['question'])
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

class QuestionOneSerializer(QuestionSerializer):
    answer = AnswerSerializerSpecific(many=True, read_only=True)

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

        if number_user_config >= 4:
             raise serializers.ValidationError({'message': 'Actualmente, solo puedes almacenar hasta 4 configuraciones.'})
        
        return attrs
    
    def create(self, validated_data):
        user = self.context['request'].user
        type_math_ids = validated_data.pop('type_math_ids', [])#sacamos los id de los tipos de ensayos de los datos validados
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

#13-09 
class PrePAESAnswerSerializer(serializers.ModelSerializer): #si pones solo serializer.Serializer solo mostrara los campos definidos como user_Essay_PrePAES, no el del moldeo

    answer_state = serializers.BooleanField(source='answers.right')
    answer_id = serializers.IntegerField(source='answers.id')

    class Meta:
        model = AnswerPrePAES
        fields = ['answer_state','answer_id']

class PrePAESQuestionSerializer(serializers.ModelSerializer): 
    
    question_id = serializers.IntegerField(source='question.id')#indicamos que queremos los id
    question_subject = serializers.CharField(source='question.subject')

    class Meta:
        model = PrePAESQuestion
        fields = ['question_id', 'question_subject']  # Campos del serializador los que se mostraran

class UserPrePAESData(serializers.ModelSerializer): #si pones solo serializer.Serializer solo mostrara los campos definidos como user_Essay_PrePAES, no el del moldeo
    user_answer = PrePAESAnswerSerializer(many=True, read_only=True, source='answers_prePAES_user')#25-09-2023 recuerda cristian que pusustte eso porque tambien podria sacar el tema de si el usuario respondio bien o mal linkeando con answerPrePAES
    user_PrePAES  = PrePAESQuestionSerializer(many=True, read_only=True, source='prePAES_question')#source el nombre de related name, indicamos que obtenga tambien los datos de este serializador dada la relación
    # Agrega más campos según sea necesario

    class Meta:
        model = PrePAES
        exclude = [*generic_fields]

    """def to_representation(self, instance):
        
        data = super().to_representation(instance)
        print(data)
        data['test'] = 'test'
        #questionState = UserQuestionState.objects.filter(question_id = questions.id, users = self.request.user) #obtenemos el estado de las preguntas 

        return data"""

class PrePAESSaveQuestionSerializer(serializers.ModelSerializer): #modificado el 12-09 para provar la obtencion de pregunta de prepaes
    # Campo 'questions' que es una lista de claves primarias relacionadas con el modelo Question

    class Meta:
        model = PrePAESQuestion
        fields = ['pre_PAES', 'question']  # Campos del serializador
    
    def create(self, validated_data):
        prePAESid = validated_data.get('pre_PAES') 
        question = validated_data.get('question') 

        prePAES_user = PrePAESQuestion.objects.create(pre_PAES_id = prePAESid.id, question_id = question.id)
        return prePAES_user


#21/27-09-2023
class PrePAESCreateSerializer(serializers.ModelSerializer): #si pones solo serializer.Serializer solo mostrara los campos definidos como user_Essay_PrePAES, no el del moldeo

    class Meta:
        model = PrePAES
        exclude = [*generic_fields]
    
    def create(self, validated_data):
        user = self.context['request'].user
        nunero_fase = PrePAES.objects.filter(user = user).count() #identifica en que fase se encuentra, si es el primero, parte en 0

        if(nunero_fase == 0):
            prePAES_user = PrePAES.objects.create(user = user, number_phase = 1) #se suma en 1 siempre el numero de fase para ser mayor que el anterior
            achievemet = Achievement.objects.filter(name = 'Iniciando el Viaje PrePAES').first()
            
            UserAchievement.objects.create(user=user, achievement=achievemet)#relacionado al primer logro que es por realizar un método prePAES
            return prePAES_user
        else:
            count = self.verifyCreation(user)
            self.verifyAchievement(user)
            if(count < 10):#si la fase aun no se completa, entonces no crea nada
                #agregar raise error
                raise serializers.ValidationError('No se han completado todas las preguntas de la fase')
            #si ya se completo entonces se crea
            if(PrePAES.objects.filter(user = user).count() == 1):
                achievemet = Achievement.objects.filter(name = 'Dominio de la Fase Inicial').first()
                UserAchievement.objects.create(user=user, achievement=achievemet)#relacionado al primer logro que es por realizar un método prePAES

            prePAES_user = PrePAES.objects.create(user = user, number_phase = nunero_fase+1) #se suma en 1 siempre el numero de fase para ser mayor que el anterior
            return prePAES_user
    
    def verifyCreation(self, user):
        queryset = PrePAES.objects.filter(user = user).order_by('-created').first()#solo el primer coincidente
        data = AnswerPrePAES.objects.filter(pre_PAES_id = queryset.id).count()#solo entrega la cuenta
        return data
    
    def verifyAchievement(self, user):

        achievemet = Achievement.objects.filter(name = 'Iniciando el Viaje PrePAES').first()
        verify = UserAchievement.objects.filter(user=user, achievement=achievemet).first()

        if(verify is None):
            UserAchievement.objects.create(user=user, achievement=achievemet)#relacionado al primer logro que es por realizar un método prePAES

#22-09-2023
class AnswerPrePAESSerializer(serializers.ModelSerializer): #si pones solo serializer.Serializer solo mostrara los campos definidos como user_Essay_PrePAES, no el del moldeo
    class Meta:
        model = Answer
        exclude = [*generic_fields, 'users', 'essay']
        
#22-09-2023
class SaveAnswerPrePAESSerializer(serializers.Serializer):
    answer_id = serializers.IntegerField()

    def create(self, data):
        
        answer = data.get('answer_id')
        user = self.context['request'].user
        
        # Crear objetos AnswerEssayUser para la respuesta seleccionada
        answer = get_object_or_404(Answer, pk=answer)
        prePAES = PrePAES.objects.filter(user=user).order_by('-created').first()

        if AnswerPrePAES.objects.filter(answers=answer, pre_PAES=prePAES, users=user).exists():
                raise serializers.ValidationError('Ya existe una respuesta para esta combinación de AnswerPrePAES y Answer.')
        
        prePAES_answer = AnswerPrePAES.objects.create(answers=answer, pre_PAES=prePAES, users=user)

        return prePAES_answer

class UserQuestionStateSerializer(serializers.ModelSerializer): #18-07 este solo se usara para mostar los datos de esta tabla, ya que como tiene elementos de otras, lo idel es usar el de abajo para crearlos
    question = QuestionSerializer()
    
    class Meta:
        model = UserQuestionState
        fields = ['state','question_id','users_id','question']

class SaveUserQuestionState(serializers.Serializer): #18-07
    answer_id = serializers.IntegerField()

    def validate(self, data):
        answer_id = data.get('answer_id')

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
                #dateF = timezone.now().replace(microsecond=0)
                #instance.updated = dateF.strftime('%Y-%m-%d %H:%M:%S')
                #print(instance.updated)
                instance.state = 'Reforzar'
                instance.is_modify = True
                instance.save()#guardamos el cambio, esto permite modificar el campo update
            else:
                instance.state = 'Correcta'
                instance.is_modify = True
                instance.save()#guardamos el cambio, esto permite modificar el campo update
        else:#si no existe creamos una instancia
            dateF = timezone.now().replace(microsecond=0)
            formatted_date = dateF.strftime('%Y-%m-%d %H:%M:%S')
            print(formatted_date)
            if answer.right == 0:
                
                instance = UserQuestionState.objects.create(question=question, users=user,state='Reforzar',created=formatted_date,updated=formatted_date)
            else:
                instance = UserQuestionState.objects.create(question=question, users=user,state='Correcta',created=formatted_date,updated=formatted_date)
        return instance


#28-09-2023
class questionTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['subject']

class StadisticsPrePAESSerializer(serializers.ModelSerializer):
    question = questionTypeSerializer()#de esta manera si la tabla posee llaves foraneas como campos
    
    class Meta:
        model = UserQuestionState
        fields = ['question','state']
    
    def to_representation(self, instance : UserQuestionState):
        
        data = super().to_representation(instance) #obtenemos la data cuando se llamara al serializador del llamado al serializador
        data['subject'] = data['question']['subject']  # Incluir el tiempo empleado en el ensayo en la representación
        data.pop('question') 

        return data

#17-10-2023
class QuestionErrorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = QuestionError
        exclude = ['created', 'updated']

#20-10-2023
class AchievmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Achievement
        exclude = [*generic_fields]

class UserAchievmentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAchievement
        exclude = [*generic_fields]

class UserAchievmentListSerializer(serializers.ModelSerializer):
    achievement = AchievmentSerializer()

    class Meta:
        model = UserAchievement
        exclude = [*generic_fields]

#03-11-2023

class validatorYoutubeULR(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['id','link_resolution']
