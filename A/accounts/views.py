from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user

# forms
from .forms import (
    UserRegistrationsForm, UserLoginForm
)


class UserRegisterView(View):
    
    def post(self, request):
        form = UserRegistrationsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(username=cd['username'], email=cd['email'], password=cd['password'])
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            user.save()
            login(request, user)
            messages.success(request, 'You registred successfully!!', 'success')
            return redirect('home')

    def get(self, request):
        form = UserRegistrationsForm()  
        return render(request, './accounts/register.html', {'form':form})


class UserLoginView(View):

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Welcome Back!', 'success')
                return redirect('home')
            else:
                messages.error(request, 'Password or Username in not valid!', 'danger')
                return render(request, './accounts/login.html', {'form':form})
            

    def get(self,request):
        form = UserLoginForm()
        return render(request, './accounts/login.html', {'form':form})
    
def logOutView(request):
    logout(request)
    messages.success(request, 'You loged out successfully!', 'success')
    return redirect('home')

def CheckUserStatus(request):
    if request.user.is_authenticated:
        context = {'user':False}
        return render(request, './base/navbar.html', context)
    
            

