from django.urls import path
from .views import *

urlpatterns = [
    path('',main,name='main'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('profile/',profile,name='profile'),
    path('add_tusk/',add_tusk,name='add_tusk')
]