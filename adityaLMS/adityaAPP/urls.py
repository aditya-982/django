from django.urls import path
from .import views

urlpatterns = [
    path("signup",views.adityaLMSUserSignUp.as_view()),
    path("getAllUser",views.adityaLMSGetUserDetails.as_view()),
    path("updateEmail",views.adityaLMSUpdateEmail.as_view()),
    path("deleteUser/<number>",views.adityaLMSDeleteUser.as_view())
]