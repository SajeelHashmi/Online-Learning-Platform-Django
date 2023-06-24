from django.shortcuts import render, redirect,HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User
# from signup.models import Student
from .models import Instructor,Course,Assignment,AssignedAssignment,SubmittedAssignment
from signup.models import Student
from django.core.exceptions import ObjectDoesNotExist
from .forms import CourseForm
from datetime import datetime
from notifications.models import Notification
from django.db.models import Count
# Create your views here.




""" complete check submissions with give assesment"""


"""assessment is updating now start working on forum app"""



# add new course view
# course Instructor view 
# 

def viewSubmissions(request,assignmentId):
    if request.user.is_authenticated:
        user = request.user
        try:
            instructor = Instructor.objects.get(user=user)
        except instructor.DoesNotExist:        
            return redirect("login")
        assignment = Assignment.objects.filter(id = assignmentId).first()
        if assignment is None:
            return redirect("instructorHome")
        course = assignment.course

        if course.instructor != instructor:
            return redirect("instructorHome")
        students = course.students.all()
        data = []
        notificationCount = Notification.objects.filter(user  = user ,read = False).count()
        if request.method =='POST':
            # print("post")
            assessment = request.POST['assessment']
            stdId = request.POST['stdId']
            std = Student.objects.filter(id = stdId).first()
            # print(std)
            submission = SubmittedAssignment.objects.filter(student =std,assignment = assignment).first()
            # print(submission)
            submission.assessment = assessment
            submission.save()
            content = "Assessment for your submission of " + assignment.title + " was marked"
            Notification.objects.create(course = course,user = user,timeStamp =datetime.now(),assignment = assignment,content = content)
        for s in students:
            info = {
            "student" :s,
            "submission" : SubmittedAssignment.objects.filter(assignment = assignment,student = s).first()
            }
            data.append(info)
            data.sort(key=lambda x: x['submission'].assessment is not None)
        return render (request,"instructor/submissions.html" , {
            "data" : data,
            "assignment":assignment,
            "notificationCount":notificationCount
})
    else:
        return redirect("login")
    

def instructorHome(request):
    if request.user.is_authenticated:
        user = request.user
        instructor = None
        try:
            instructor = Instructor.objects.get(user=user)
        except ObjectDoesNotExist:        
            return redirect("login")
        courses = Course.objects.filter(instructor = instructor)
        notificationCount = Notification.objects.filter(user  = user ,read = False).count()

        return render(request,"instructor/home.html",
                      {
                          "instructor":instructor,
                          "courses":courses,
                        "notificationCount":notificationCount

                      })
    else:
        return redirect("login")
    
# display course information 
# show all students enrolled 
# upload assignment 
# view submissions for an assignment
# assesments



# assignment being created and assigned to students#
def newAssignment(request):
    if request.user.is_authenticated:
        user = request.user
        instructor = None
        try:
            instructor = Instructor.objects.get(user=user)
        except ObjectDoesNotExist:
            return redirect("login")
        
        if instructor is None:
            return redirect("login")
        if request.method == "POST":
            courseId = request.POST['courseId']
            course_url = reverse('courseDashboard', args=[courseId])
            dueDate = request.POST['dueDate']
            title = request.POST['title']
            file = request.FILES['file']
            course= Course.objects.filter(id = courseId).first()
            assignment = Assignment.objects.create(course = course,due_date = dueDate,title = title,file=file )
            messages.success(request, "New Assignment has been Uploaded")
            students = course.students.all()
            # print 
            content = "New assignment for " + course.title + "has been uploaded with due date " + str(assignment.due_date)
            for s in students:
                Notification.objects.create(course = course,user = s.user,timeStamp =datetime.now(),assignment = assignment,content = content)
                AssignedAssignment.objects.create(assignment = assignment,student = s)

            return redirect(course_url)
        return redirect ('instructorHome')
    else:
        return redirect("login")



def courseDashboard(request,courseId):
    if request.user.is_authenticated:
        user = request.user
        try:
            instructor = Instructor.objects.get(user=user)
        except instructor.DoesNotExist:        
            return redirect("login")
        course = Course.objects.filter(id = courseId).first()
        notificationCount = Notification.objects.filter(user  = user ,read = False).count()
        assignments = Assignment.objects.filter(course = course)
        return render(request,'instructor/course.html',{
            "course":course,
            "assignments":assignments,
            "notificationCount":notificationCount
            })
    else:
        return redirect("login")



# add a new course
# Done and working#
def newCourse(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            instructor = Instructor.objects.get(user=user)
        except instructor.DoesNotExist:        
            return redirect("login")
        if request.method == 'POST':
            form = CourseForm(request.POST, instructor=request.user.instructor)
            if form.is_valid():
                course = form.save()
                tags = form.cleaned_data.get('tags')
                course.save()
                if tags:
                    course.tags.set(tags)
                return redirect('instructorHome')
        form = CourseForm(instructor=request.user.instructor)

        return render(request,'instructor/newCourse.html',{'form':form})
    else:
        return redirect("login")
