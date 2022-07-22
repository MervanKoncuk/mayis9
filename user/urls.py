from django.urls import path
from .views import *
urlpatterns = [
    path("login/", giris, name="login"),
    path("register/", kayit, name="register"),
    path("logout/", userLogout, name="logout")
]

