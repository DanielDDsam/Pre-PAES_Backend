import datetime
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)



common_args = {'null': True, 'blank': True} #atributos generales que tienen que tener

#Clase abstracta para que todas las clases que hereden de ella tengan los mismos atributos
class GenericAttributes(models.Model):
    created = models.DateTimeField(**common_args, auto_now_add=True, editable=False)  # para saber cuando fue creado el dato
    updated = models.DateTimeField(**common_args, auto_now=True) # para saber cuando se actualizo el dato
    is_deleted = models.BooleanField(**common_args, default=False) #para un borrado logico de las vistas no borrado fisico de la bd

    class Meta:
        abstract = True


# Clase del modelo UserManager
class UserManager(BaseUserManager):

    def _create_user(self, email, username, is_admin, is_active, password=None):
        print(is_admin)
        user = self.model(
            email=self.normalize_email(email),
            username = username,
            is_admin = is_admin,
            is_active = is_active, 
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        return self._create_user(
            email,
            username, 
            False,
            True, 
            password
        )

    def create_superuser(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        
        return self._create_user(
            email,
            username,
            True,
            True, 
            password
        )

#Clase del modelo Users
class Users(AbstractBaseUser,GenericAttributes):
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    is_admin = models.BooleanField(**common_args,default=False)
    username = models.TextField(**common_args)
    is_active = models.BooleanField(**common_args, default = True)
    #schoolType = models.CharField(**common_args, max_length=255)
    #academicDegree = models.CharField(**common_args, max_length=255)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin


# Clase del modelo Essay
class MathType(GenericAttributes):
    name = models.TextField(**common_args)
    type = models.TextField(**common_args)


# Clase del modelo CustomEssay
class CustomEssay(GenericAttributes):
    is_custom = models.BooleanField(default=False)
    name = models.TextField(**common_args)
    type_essay = models.ManyToManyField(MathType, blank=True, through='TypesEssayCustom', related_name='custom_type_essay')
    user = models.ForeignKey(Users, **common_args, on_delete=models.CASCADE, related_name='essay_user')
    current_questions = models.IntegerField(**common_args)
    prePaes = models.BooleanField(default=False)#10-08-2023


# Clase del modelo EssayAnswer
class TypesEssayCustom(GenericAttributes):
    type_essays = models.ForeignKey(MathType, **common_args,on_delete=models.CASCADE, related_name='type_essay_custom')
    custom_essay = models.ForeignKey(CustomEssay, **common_args,on_delete=models.CASCADE, related_name='essay_custom')


# Clase del modelo Question
class Question(GenericAttributes):
    question = models.TextField(**common_args)
    subject = models.TextField(**common_args)
    link_resolution = models.URLField(**common_args, unique=True)
    type_question = models.ForeignKey(MathType, **common_args,on_delete=models.CASCADE, related_name='question_type')
    users = models.ManyToManyField(Users, blank=True, through='UserQuestionState', related_name='question_user') #18-07

# Clase del modelo UserQuestionState
class UserQuestionState(GenericAttributes): #18-07
    question = models.ForeignKey(Question, **common_args, on_delete=models.CASCADE,related_name='user_question_state')
    users = models.ForeignKey(Users, **common_args, on_delete=models.CASCADE, related_name='user_question_state')
    state = models.TextField(**common_args)


# Clase del modelo CustomEssayQuestion
class CustomEssayQuestion(GenericAttributes):
    custom_essay = models.OneToOneField(CustomEssay, on_delete=models.CASCADE)
    question = models.OneToOneField(Question, on_delete=models.CASCADE)


# Clase del modelo Answer
class Answer(GenericAttributes):
    label = models.CharField(**common_args, max_length=255)
    right = models.IntegerField(**common_args)
    questions = models.ForeignKey(Question, **common_args, on_delete=models.CASCADE, related_name='answer')
    users = models.ManyToManyField(Users, blank=True, through='AnswerEssayUser', related_name='answer')
    essay = models.ManyToManyField(CustomEssay, blank=True, through='AnswerEssayUser', related_name='answer')


# Clase del modelo AnswerEssayUser
class AnswerEssayUser(GenericAttributes):
    answers = models.ForeignKey(Answer, **common_args, on_delete=models.CASCADE, related_name='answers_essay_user')
    essays = models.ForeignKey(CustomEssay, **common_args, on_delete=models.CASCADE, related_name='answers_essay_user')
    users = models.ForeignKey(Users, **common_args, on_delete=models.CASCADE, related_name='answers_essay_user')
    score = models.IntegerField(**common_args)
    time_essay = models.TextField(**common_args)

class UserEssayConfig(GenericAttributes): #25-07
    name = models.TextField(**common_args)
    users = models.ForeignKey(Users, **common_args, on_delete=models.CASCADE, related_name='user_Essay_Config')
    essays_types = models.ManyToManyField(MathType, blank=True, through='UserEssayConfigTypes', related_name='user_Essay_Config')
    questionNumber = models.IntegerField(**common_args)

class UserEssayConfigTypes(GenericAttributes): #25-07
    users_essasy_config = models.ForeignKey(UserEssayConfig, **common_args, on_delete=models.CASCADE, related_name='user_Essay_Config_types')
    essay_types = models.ForeignKey(MathType, **common_args, on_delete=models.CASCADE, related_name='user_Essay_Config_types')

    