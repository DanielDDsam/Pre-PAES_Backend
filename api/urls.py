from api import views
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from rest_framework_simplejwt.views import (TokenObtainPairView,)
from rest_framework_simplejwt import views as jwt_views


#RESTful endpoints
urlpatterns = [
    re_path(r'^user(s)?/all/$', views.UsersListCreate.as_view()),#Endpoint para consultar listado de usuarios
    re_path(r'^user(s)?/(?P<pk>[0-9]+)/$', views.UsersRetrieveUpdateDestroy.as_view()),#Endpoint para consultar, eliminar, actualizar un usuario específico
    re_path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),#Endpoint para obtener un token
    re_path('api/register/', views.RegisterView.as_view(), name='register'),#Endpoint para registrar usuario
    re_path('api/register_admin/', views.RegisterAdminView.as_view(), name='registerAdmin'),#Endpoint para registrar usuario
    re_path('api/login/', views.LoginView.as_view(), name='login'),#Endpoint para iniciar sesión
    re_path('api/logout/', views.LogoutView.as_view(), name='logout'),#Endpoint para cerrar sesión
    re_path('api/token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),#Endpoint para refrescar el token

    re_path(r'^essays/list/all/$', views.EssayList.as_view()),#Endpoint para consultar todos los tipos de ensayos
    re_path(r'^essays/create/$', views.EssayCreate.as_view()),#Endpoint para crear un ensayo
    re_path(r'^essays/(?P<pk>[0-9]+)/$', views.EssayRetrieveUpdateDestroy.as_view()),#Endpoint para consultar, eliminar, actualizar un ensayo específico

    re_path(r'^essaysConfig/create/$', views.UserEssayConfigCreate.as_view()),#Endpoint para guardar la configuración del esayo para usuario
    re_path(r'^essaysConfig/list/$', views.UserEssayConfigList.as_view()),#Endpoint para listar las configuraciones de los esayos para usuario
    re_path(r'^essaysConfig/retrieve/(?P<pk>[0-9]+)/$', views.UserEssayConfigRetrieveUpdate.as_view()),#Endpoint para consultar, eliminar, actualizar una configuracion de ensayo personalizado

    re_path(r'^questions/list/all/$', views.QuestionList.as_view()),#Endpoint para consultar todas las preguntas
    re_path(r'^questions/create/$', views.QuestionCreate.as_view()),#Endpoint para crear una pregunta
    re_path(r'^questions/(?P<pk>[0-9]+)/$', views.QuestionRetrieveUpdateDestroy.as_view()),#Endpoint para consultar, eliminar, actualizar una pregunta específica
    re_path(r'^questions_types/(?P<tiposDePreguntas>[^/]+)/(?P<numeroDePreguntas>\d+)/$', views.QuestionListType.as_view()),#Endpoint para consultar preguntas en base a tipos
    re_path(r'^questions/dificult/$', views.QuestionDificultJson.as_view()),#Endpoint para consultar, eliminar, actualizar una pregunta específica

    re_path(r'^answers/list/all/$', views.AnswerList.as_view()),#Endpoint para consultar todas las respuestas
    re_path(r'^answers/create/$', views.AnswerCreate.as_view()),#Endpoint para crear una respuesta
    re_path(r'^answers/(?P<pk>[0-9]+)/$', views.AnswerRetrieveUpdateDestroy.as_view()),#Endpoint para consultar, eliminar, actualizar una respuesta específica

    re_path(r'^questions_alternativeSpecific/(?P<pk>[0-9]+)/$', views.questionAnswers.as_view()),#endpoint para consultar por una pregunta especifica y sus alternativas
    re_path(r'^question_oneQuestion/$', views.oneQuestion.as_view()),#endpoint para consultar una sola pregunta de manera aleatoria
    re_path(r'^question_oneQuestionRules/$', views.oneQuestionRules.as_view()),#endpoint para consultar una sola pregunta en base a las reglas establecidas   
    re_path(r'^questions_alternative/$', views.QuestionsAlternativeAllView.as_view()),#Endpoint para consultar todas las preguntas y alternativas respectivas
    re_path(r'^questions_error/$', views.questionErrorListCreateView.as_view()),#Endpoint para consultar todos los errores 
    re_path(r'^questions_error/admin/(?P<pk>[0-9]+)/$', views.questionErrorRetrieveUpdateDestroyView.as_view()),#Endpoint para consultar, eliminar, actualizar un error en especifico
    re_path(r'^questions_url_validator/$', views.validatorURLView.as_view()),#Endpoint para consultar, eliminar, actualizar un error en especifico


    re_path(r'^score_user/all/$', views.AnswerEssayUserView.as_view()),#Endpoint para obtener el puntaje del usuario en un esayo especifico
    re_path(r'^submit_answers/$', views.SaveAnswersView.as_view()),#Endpoint para guardar las respuestas del usuario en un esayo especifico

    re_path(r'^submit_one_answers/$', views.SaveOneAnswer.as_view()),#Endpoint para guardar una respuesta del usuario
    re_path(r'^submit_answer_state/$', views.SaveUserQuestion.as_view()),#Endpoint para guardar el estado de la respuesta del usuario

    re_path(r'^history/(?P<pk>[0-9]+)/$', views.UserEssayHistoryView.as_view()),#Endpoint para consultar el historial de ensayos de un usuario en especifico
    re_path(r'^custom_essay_view/(?P<pk>[0-9]+)/$', views.CustomEssayResponseView.as_view()),#Endpoint para consultar un ensayo mediante su id entregal o que se respondio
    re_path(r'^custom_essays/$', views.CustomEssayView.as_view()),#Endpoint para consultar y crear ensayos personalizados
    re_path(r'^submit_questions/$', views.CustomEssayQuestionView.as_view()),#Endpoint para asociar preguntas a un ensayo personalizado o predeterminado

    re_path(r'^PrePAES/verify/$', views.PrePAESListExistView.as_view()),#Endpoint para verificar si el usuario actual posee ensayos PrePAES
    re_path(r'^PrePAES/create/$', views.PrePAESCreateView.as_view()),#Endpoint para crear ensayos prePAES
    re_path(r'^PrePAES_questions_state/$', views.UserPrePAESQuestionsListViews.as_view()),#Endpoint para obtener el estado (correcta, incorrecta) de todas las pregunta que ha respondido de prePAES
    re_path(r'^PrePAES_questions_state/(?P<fase>[0-9]+)/$', views.UserPrePAESQuestionsListViews.as_view()),#Endpoint para obtener el estado (correcta, incorrecta) de todas las pregunta que ha respondido de prePAES en una fase
    re_path(r'^question_oneQuestionRules_prePaes/$', views.oneQuestionRulesPrePaes.as_view()),#endpoint para consultar una sola pregunta en base a las reglas establecidas para el algoritmo de adaptabilidad
    re_path(r'^PrePAES_submit_answers/$', views.AnswerPrePAESView.as_view()),#guarda una respuesta del usuario para método prePAES
    re_path(r'^PrePAES_data_questions/(?P<question>[0-9]+)/$', views.oneQuestionDataListView.as_view()),#endpoint para consultar la pregunta con todos sus datos
    re_path(r'^PrePAES_stadictis/$', views.stadisticsPrePAESView.as_view()),#endpoint para consultar las estadisticas de resumen del método prePAES para un usuario especifico
    re_path(r'^PrePAES_stadictis_real_time/(?P<fase>[0-9]+)/$$', views.stadisticsPrePAESRealTimeView.as_view()),#endpoint para consultar las estadisticas en tiempo real para la fase actual de prePAES
    #para obtener las demas respuestas usar la url questions_alternativeSpecific
    re_path(r'^PrePAES_answers/(?P<question>[0-9]+)/$', views.AnswerPrePAESListView.as_view()),#Endpoint para obtener todas las respuestas de una pregunta en prePAES

    re_path(r'^best_average_score/(?P<pk>[0-9]+)/$', views.bestAverageScore.as_view()),#Endpoint para consultar el puntaje maximo y el promedio de puntajes de un usaurio
    re_path(r'^recent_essay/(?P<pk>[0-9]+)/$', views.CustomEssayMostRecentView.as_view()),#Endpoint para consultar el ensayo más reciente
    re_path(r'^recent_essay_resume/(?P<pk>[0-9]+)/$', views.CustomEssayMostRecentResumeView.as_view()),#Endpoint para consultar los ultimos 5 ensayos
    re_path(r'^percentage_math_type/$', views.questionPercentView.as_view()),#Endpoint para determinar el porcentaje de correstas y erroneas dependiendo de las categorias

    re_path(r'^achievment/$', views.achievmentListCreateView.as_view()),#Endpoint para crear y listar logros de un usuario
    re_path(r'^achievment/(?P<pk>[0-9]+)/$', views.achievmenRetrieveUpdateDestroyView.as_view()),#Endpoint para modificar, eliminar y retornar solo uno logro
    re_path(r'^achievment_user/create/$', views.UserAchievmentCreateView.as_view()),#Endpoint para asociar un logro a un usuario
    re_path(r'^achievment_user/$', views.UserAchievmentListView.as_view()),#Endpoint para retornar todos los logros de un usuario

    re_path(r'^home/$', views.falseCharge.as_view()),#Endpoint para peticion falsa
]

urlpatterns += [
    re_path(r'^api/send_reset_password_email/$', views.SendPasswordResetEmailView.as_view(), name='send_reset_password_email'),#Endpoint para pedir un cambio de contraseña via mail
    path('api/reset_password/<uid>/<token>/', views.UserPasswordResetView.as_view(), name='reset_password'),#Endpoint para cambiar la contraseña si se tiene uid y el token asignado
    re_path(r'^api/change_password/$', views.ChangePasswordView.as_view(), name='change_password'),#Endpoint para cambiar la contraseña
    re_path(r'^api/change_password_profile/$', views.ChangeProfilePasswordView.as_view(), name='change_password_profile'),#Endpoint para cambiar la contraseña en la vista de perfil
    re_path(r'^api/profile/$', views.UserProfileView.as_view(), name='profile'),#Endpoint para consultar el perfil del usuario

]

