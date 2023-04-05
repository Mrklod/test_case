from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from django.contrib import auth
from .forms import UserRegisterForm,UserLoginForm,ProfileForm,TuskForm
from .models import Tusk
from django.utils.decorators import method_decorator
from django.views import View


class MainView(View):
    def get(self,request):
        context = {'title': 'Главная'}
        if request.user.is_authenticated:
            author = request.user
            content = Tusk.objects.filter(author=author)
            context['tusk'] = content
        return render(request, 'tusk/main.html', context=context)


class RegisterView(View):
    def get(self,request):
        form = UserRegisterForm
        context = {'form': form, 'title': 'Регистрация'}
        return render(request, 'tusk/register.html', context=context)

    def post(self,request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('login'))



class LoginView(View):
    def get(self,request):
        form = UserLoginForm
        context = {'form': form, 'title': 'Авторизация'}
        return render(request, 'tusk/login.html', context=context)

    def post(self,request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse_lazy('main'))
        context = {'form': form, 'title': 'Авторизация'}
        return render(request, 'tusk/login.html', context=context)


@method_decorator(login_required,name='dispatch')
class LogoutView(View):
    def get(self,request):
        auth.logout(request)
        return redirect(reverse_lazy('main'))

@method_decorator(login_required,name='dispatch')
class ProfView(View):

    def get(self,request):
        form = ProfileForm(instance=request.user)
        context = {'form':form,'title':'Личный профиль'}
        return render(request,'tusk/profile.html',context=context)

    def post(self,request):
        prof = request.user
        form = ProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            prof.username = request.POST['username']
            prof.email = request.POST['email']
            prof.phone = request.POST['phone']
            prof.save()
        context = {'form': form, 'title': 'Личный профиль'}
        return render(request, 'tusk/profile.html', context=context)

@method_decorator(login_required,name='dispatch')
class AddTuskView(View):
    def get(self,request):
        form = TuskForm
        context = {'title':'Добавление задачи','form':form}
        return render(request,'tusk/add_tusk.html',context=context)

    def post(self,request):
        us = request.user
        form = TuskForm(request.POST)
        if form.is_valid():
            tusk = form.save(commit=False)
            tusk.author_id = request.user.id
            tusk.save()
            us.point = us.point + 1
            us.save()
            return HttpResponseRedirect(reverse_lazy('main'))


@method_decorator(login_required,name='dispatch')
class DeletePostView(View):
    def post(self,request,pk):
        us = request.user
        tusk = get_object_or_404(Tusk,pk=pk)
        if tusk.author == request.user:
            tusk.delete()
            us.point = us.point - 1
            us.save()
        return redirect('main')


@method_decorator(login_required,name='dispatch')
class UpdatePostView(View):
    def get(self,request,pk):
        tusk = get_object_or_404(Tusk,pk = pk)
        form = TuskForm(instance=tusk)
        context = {'title': 'Обновление задач', 'form': form, 'tusk': tusk}
        return render(request, 'tusk/change_tusk.html', context=context)

    def post(self,request,pk):
        us = request.user
        tusk = get_object_or_404(Tusk,pk = pk)
        form = TuskForm(request.POST,instance=tusk)
        if form.is_valid():
            tusk.title = request.POST['title']
            tusk.text = request.POST['text']
            tusk.save()
            us.point = us.point + 0.5
            us.save()
            return HttpResponseRedirect(reverse_lazy('main'))
        context = {'title': 'Обновление задач', 'form': form, 'tusk': tusk}
        return render(request, 'tusk/change_tusk.html', context=context)

