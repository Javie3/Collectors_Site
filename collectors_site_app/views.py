from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt

# def index(request):
#     return HttpResponse("It's working!")


#Renders Index#
def index(request):
    return render(request, "index.html")


  
#process the user Info 
def process(request):
    print(request.POST)
    #Creates User and makes sure password match's with if statement#
    if request.POST['pw'] != request.POST['confpw']:
        return redirect('/')
    else: 
        errors = User.objects.basic_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')   
        new_user = User.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], email=request.POST['email'], password=request.POST['pw'])
        request.session['user'] = new_user.first_name
        request.session['id'] = new_user.id
        return redirect('/')


#logins in User
def login(request):
    print(request.POST)
    logged_user = User.objects.filter(email=request.POST['email'])
    if len(logged_user) > 0:
        logged_user = logged_user[0]
        if logged_user.password == request.POST['pw']:
            request.session['user'] = logged_user.first_name
            request.session['id'] = logged_user.id
        return redirect('/success')
    return redirect('/')

  