from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
from .models import *

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={}))
    class Meta:
        model = Users
        fields = ('username','password')

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput())
    phone = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Users
        fields = ('username','phone','email','password1','password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('username','email','phone')

