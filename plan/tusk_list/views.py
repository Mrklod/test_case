from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import auth
from .forms import UserRegisterForm,UserLoginForm,ProfileForm
from .models import Tusk

def main(request):
    tusk_list = Tusk.objects.all()
    context = {'tusk':tusk_list}
    return render(request,'tusk/main.html',context=context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserRegisterForm()
    context = {'form':form}
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
    context = {'form':form}
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
    context = {'form':form}
    return render(request,'tusk/profile.html',context=context)