from atexit import register
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('signin/', views.signin, name="signin"),
    path('register/', views.register, name="register"),
    path('signout/', views.signout, name="signout")
]