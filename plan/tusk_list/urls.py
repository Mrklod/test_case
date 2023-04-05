from django.urls import path
from .views import *

urlpatterns = [
    path('',MainView.as_view(),name='main'),
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('profile/',ProfView.as_view(),name='profile'),
    path('add_tusk/',AddTuskView.as_view(),name='add_tusk'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='delete_post'),
    path('post/<int:pk>/update/', UpdatePostView.as_view(), name='update_post'),
    path('tops/',TopUsersView.as_view(),name='top')
]
