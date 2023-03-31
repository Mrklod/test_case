from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,'tusk/base.html')

def register(request):
    return render(request,'tusk/register.html')

def login(request):
    return render(request,'tusk/login.html')

def profile(request):
    return render(request,'tusk/profile.html')