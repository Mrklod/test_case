from django.urls import path
from .views import *

urlpatterns = [
    path('',main,name='main'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('profile/',ProfView.as_view(),name='profile'),
    path('add_tusk/',AddTuskView.as_view(),name='add_tusk'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='delete_post'),
    path('post/<int:pk>/update/', UpdatePostView.as_view(), name='update_post'),
]
