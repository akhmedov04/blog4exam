from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import *
from django.views import View
from .forms import *


class LoginView(View):
    def post(self,request):
            user = authenticate(username=request.POST.get('u'),
                                password=request.POST.get('p'))
            if user is None:
                return redirect('/')
            login(request, user)
            return redirect('/blogs/')
    def get(self, request):
        return render(request, 'login.html')


class RegisterView(View):
    def post(self, request):
        if request.POST.get('p') == request.POST.get('cp'):
            User.objects.create_user(
                username=request.POST.get('l'),
                password=request.POST.get('p')
            )
            return redirect('/')
    def get(self, request):
        return render(request,'register.html')

class BlogView(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = Muallif.objects.get(user_fk=request.user)
            data = {
                'maqolalar':Maqola.objects.filter(muallif=user)
            }
            return render(request, 'blogs.html', data)
        return redirect('/')


class MaqolaView(View):
    def get(self, request, id):
        user = Muallif.objects.get(user_fk=request.user)
        data = {
            "maqola": Maqola.objects.filter(muallif=user, id=id)
        }
        return render(request, "maqola.html", data)

def logoutview(request):
    logout(request)
    return redirect('/')
