from django.urls import path
from .views import *

urlpatterns = [
    path('',main,name='main'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('profile/',profile,name='profile')
]