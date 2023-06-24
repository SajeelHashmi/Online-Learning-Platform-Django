from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from instructorDashboard .models import Instructor,Course
from .models import Forum,Post,Reply
from django.core.exceptions import ObjectDoesNotExist
from signup.models import Student
from notifications.models import Notification

from datetime import datetime

# Create your views here.






def newReply(request):
    isInstructor = True
    instructor = None
    if request.user.is_authenticated:
        user = request.user
        try:
            instructor = Instructor.objects.get(user=user)
        except ObjectDoesNotExist:  
            isInstructor = False
        if request.method =="POST":
            forumId = request.POST["forumId"]
            postId = request.POST["postId"]
            content = request.POST["content"]
            post = Post.objects.filter(id = postId).first()
            print(post)
            Reply.objects.create(post = post,author  = user ,content = content,uploadTime = datetime.now())
            content = user.username + " replied to your post: " + post.title
            Notification.objects.create(user = post.author,course = post.forum.course , timeStamp = datetime.now(),post = post,content = content)
            url = reverse ("forum",args=[forumId])
            return redirect(url)
                    
    else:
        return redirect("login")
    
    

def newPost(request):
    isInstructor = True
    instructor = None
    if request.user.is_authenticated:
        user = request.user
        try:
            instructor = Instructor.objects.get(user=user)
        except ObjectDoesNotExist:  
            isInstructor = False
        if request.method =="POST":
            forumId = request.POST["forumId"]
            forum = Forum.objects.filter(id = forumId).first()
            title = request.POST["title"]
            content = request.POST["content"]
            post = Post.objects.create(forum = forum,author=user,title = title,content = content,uploadTime = datetime.now())
            course = forum.course
            if isInstructor:
                students = course.students.all()
                content = post.title + " new post from instructor of " + course.title
                for s in students:
                    Notification.objects.create(course = course,user = s.user,timeStamp = datetime.now(),post = post,content = content )
            else:
                content = user.username + " posted in forum for course " + course.title
                Notification.objects.create(course = course,user = course.instructor.user,timeStamp = datetime.now(),post = post,content = content )
            url = reverse ("forum",args=[forumId])
            return redirect(url)
    else:
        return redirect("login")
    


def forum(request,courseId):
    isInstructor = True
    instructor = None
    if request.user.is_authenticated:
        user = request.user
        try:
            instructor = Instructor.objects.get(user=user)
        except ObjectDoesNotExist:  
            isInstructor = False
        course = Course.objects.filter(id = courseId).first()
        if course is None:
            print("courseisnoe")
            return redirect("home")
        if isInstructor:
            if course.instructor.user != user:
                print("nowinstructor")
                return redirect('home')
        else:
            student = Student.objects.filter(user = user).first()
            # print(course.students.all())
            if student not in course.students.all():
                print("not in students")
                return redirect("home")

        forum = Forum.objects.filter(course = course).first()
        post = Post.objects.filter(forum = forum).order_by("-uploadTime")
        posts = []
        for p in post:
            data ={
                "post":p,
                "replies": Reply.objects.filter(post = p).order_by("-uploadTime")
            }
            posts.append(data)
        notificationCount = Notification.objects.filter(user  = user ,read = False).count()

        print(forum)
        # create forum object
        # get details via course
        # render details in template#
        return render( request , "forum/home.html",{
            "isInstructor":isInstructor,
            "forum":forum,
            "posts":posts,
            "notificationCount":notificationCount

        })
    else:
        return redirect("login")