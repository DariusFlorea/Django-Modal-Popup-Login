from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
from django.contrib import messages


   # Login Page
def Login(request):
   if request.user.is_authenticated:
       return redirect('/')
   else:
       messages.info(request, 'Please, login first.') 
       return redirect('/')  

# Login User
def LoginUser(request):
    if request.method == 'POST':
        email = request.POST['email'] 
        password = request.POST['password'] 
        user = authenticate( email=email, password=password)
        if user != None: 
            login(request, user)
            messages.success(request, 'You are login')
            data = {'login': "Succes"}  
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request, 'You username or password dont match')
            data = {'email': "nouser"}
            return redirect(request.META['HTTP_REFERER'])
    else:
        data = {}
        messages.info(request, 'Please, login first')
        return redirect('home')
   
# Logout   
def LogoutUser(request):
   logout(request)
   messages.success(request, 'You have been logout')
   return redirect(request.META['HTTP_REFERER'])    
