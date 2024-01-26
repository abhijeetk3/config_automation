from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("login/", views.login_page, name="loginpage"),
    path("logout/", views.logout_page, name="logoutpage"),
]