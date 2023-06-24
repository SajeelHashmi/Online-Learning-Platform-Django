from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Student
import os
# from django.contrib.auth import normalize_email

# Create your views here.
# normalize email left

def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # if user.is_active:
            login(request, user)
            #return redirect('home')  # Redirect to the desired page after successful login
            return redirect("home")
        else:
            messages.success(request=request,message="incorrect user name or password")
            return redirect('login')
    else:
        return render(request , 'login.html', {})


def logout_user(request):
    logout(request=request)
    return redirect("login")


def sign_up(request):
    if request.method =="POST":
        # print("method post")
        username = request.POST["username"]
        email = request.POST["email"]
        pass2 = request.POST["pass2"]
        pass1 = request.POST["pass1"]
        image = request.FILES["image"]
        
        print(username)
        print(email)
        print(pass2)
        print(pass1)
        print(image)

        normalized_email = email.lower()   
        # validate the data in the form
        if pass1==pass2:
            user = User.objects.create_user(username=username, password=pass1,email=normalized_email)
            user.save()
            student = Student.objects.create(user = user)
            if image:
                student.image = image
            student.save()
            login(request,user)
            return redirect("home")
        else:
            messages.success(request=request,message="PASSWORDS DONOT MATCH")
    return render(request,"signup.html")