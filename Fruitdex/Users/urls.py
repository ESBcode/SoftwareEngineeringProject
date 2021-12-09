from  django.urls import path
from . import views


# app_name = 'Users'
urlpatterns = [
    path("", views.user_profile,name= "profile"),
    path("signup", views.signup_view, name ="signup"),
    path("login", views.login_view, name = 'login-view'),
]