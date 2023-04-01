from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import auth
from .forms import UserRegisterForm,UserLoginForm,ProfileForm,TuskForm
from .models import Tusk

def main(request):
    context = {'title': 'Главная'}
    if request.user.is_authenticated:
        author = request.user
        content = Tusk.objects.filter(author=author)
        context['tusk'] = content
    return render(request,'tusk/main.html',context=context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserRegisterForm()
    context = {'form':form,'title':'Регистрация'}
    return render(request,'tusk/register.html',context=context)

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user:
                auth.login(request,user)
                return HttpResponseRedirect(reverse('main'))
    else:
        form = UserLoginForm()
    context = {'form':form,'title':'Авторизация'}
    return render(request,'tusk/login.html',context=context)

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))

@login_required
def profile(request):
    prof = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            prof.username = request.POST['username']
            prof.email = request.POST['email']
            prof.phone = request.POST['phone']
            prof.save()
    else:
        form = ProfileForm
    context = {'form':form,'title':'Личный профиль'}
    return render(request,'tusk/profile.html',context=context)

@login_required
def add_tusk(request):
    if request.method == 'POST':
        form = TuskForm(request.POST)
        if form.is_valid():
            print(2)
            tusk=form.save(commit=False)
            tusk.author_id = request.user.id
            tusk.save()
            print(1)
            return HttpResponseRedirect(reverse('main'))
    else:
        print(2)
        form = TuskForm
    context = {'title':'Добавление задачи','form':form}
    return render(request,'tusk/add_tusk.html',context=context)