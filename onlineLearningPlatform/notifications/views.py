from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from instructorDashboard .models import Instructor,Course
from django.core.exceptions import ObjectDoesNotExist
from signup.models import Student
from .models import Notification
# Create your views here.

# show notification count on home page
# make notifications whenever instructor posts on forum
# make notification when someone replies to our post on forum
# make notification when an assignment is added to a course
# make notification when an assignment is assesed by the instructor#




def notifications(request):
    isInstructor = True
    instructor = None
    if request.user.is_authenticated:
        user = request.user
        try:
            instructor = Instructor.objects.get(user=user)
        except ObjectDoesNotExist:  
            isInstructor = False
        
        notifications = Notification.objects.filter(user = user).order_by("-timeStamp")


        return render(request, "notifications/notification.html",{
            "isInstructor":isInstructor,
            "notifications":notifications
            })
    else:
        return redirect("login")
    
def markAsRead(request,id):
    isInstructor = True
    instructor = None
    if request.user.is_authenticated:
        user = request.user
        try:
            instructor = Instructor.objects.get(user=user)
        except ObjectDoesNotExist:  
            isInstructor = False
        
        checkList = Notification.objects.filter(user = user).order_by("-timeStamp")
        notification = Notification.objects.filter(id = id).first()
        if notification in checkList:
            notification.read =True
            notification.save()

        return redirect('notifications')
    else:
        return redirect("login")