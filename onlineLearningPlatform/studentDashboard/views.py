from django.shortcuts import render, redirect,HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from signup.models import Student
from instructorDashboard.models import Assignment,SubmittedAssignment,Course
from datetime import date,datetime
from notifications.models import Notification
from django.db.models import Count


# student course<course_id> view
# offered courses view



# student dashboard view courses enroll submit assignments
# now left is notifications for students and course forums 
# both are different apps but some integration will be required
# after finishing all then add integration of jazz cash api#



def studentHome(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            student = Student.objects.get(user=user)
        except Student.DoesNotExist:        
            return redirect("instructorHome")
        courses = student.courses.all()
        coursesInfo = []
        notificationCount = Notification.objects.filter(user  = user ,read = False).count()
        for c in courses:
            data = {
                "course":c,
                 "totalAssignments" : Assignment.objects.filter(course=c).count(),
                "submittedAssignments" : SubmittedAssignment.objects.filter(assignment__course=c, student=student).count()

            }
            coursesInfo.append(data)
        # print(notificationCount)
    
        return render(request,"student/home.html",{
            "student":student,
            "coursesInfo": coursesInfo,
            "notificationCount":notificationCount
            })
    else:
        return redirect("login")

def submitAssignment(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            student = Student.objects.get(user=user)
        except Student.DoesNotExist:        
            return redirect("instructorHome")
        if request.method =="POST":
            courseId = request.POST['courseId']
            assignmentId = request.POST['assignmentId']
            assignment = Assignment.objects.filter(id = assignmentId).first()
            submission = request.FILES['submission']
            SubmittedAssignment.objects.create(assignment =assignment,student = student,submission_file = submission)
            messages.success(request, "Assignment has been submitted")
            course_url = reverse('course', args=[courseId])
            print(course_url)
            return redirect(course_url)
        else:
            return redirect("home")
def offeredcourses(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            student = Student.objects.get(user=user)
        except Student.DoesNotExist:        
            return redirect("instructorHome")
        tag = request.GET.get('tag')
        sort = request.GET.get("sort_by")
        keyword = request.GET.get('search')
        courses = Course.objects.all()
        if tag:
            courses = courses.filter(tags__name=tag)

        if keyword:
            courses = courses.filter(title__icontains=keyword)
        match sort:
            case "price_low_high":
                courses = courses.order_by('price')
            case "price_high_low":
                courses = courses.order_by('-price')
            case "start_date_low_high":
                courses = courses.order_by('start_date')
            case "start_date_high_low":
                courses = courses.order_by('-start_date')

        notificationCount = Notification.objects.filter(user  = user ,read = False).count()

        print(courses)
        # there must be better way to get tags 
        # tags= Tag.objects.filter(course = course)

        return render(request,"student/offeredcourses.html",{
            "courses":courses,
            "notificationCount":notificationCount
            })
    else:
        return redirect("login")





# embed a payment system all else is done#
def enrollCourse(request):
    if request.method =="POST":
        courseId = request.POST['courseId']
        print(courseId)
    else:
        return redirect('home')
    if request.user.is_authenticated:
        user = request.user
        try:
            student = Student.objects.get(user=user)
        except Student.DoesNotExist:        
            return redirect("instructorHome")
        course = Course.objects.filter(id = courseId).first()
        if course is None:
            return redirect("home")
        course_url = reverse('course', args=[courseId])

        if student in course.students.all():
            messages.success(request,"you are already inerolled in this course")
            # print(course_url)
            return redirect(course_url)
        today = date.today()
        if course.start_date > today or course.start_date == today:
            course.students.add(student)
            messages.success(request, "You have been enrolled in the course successfully.") 
            return redirect(course_url)
        messages.error(request,"The start date for this course has already passed try enrolling when next session")
        return redirect(course_url)

# use same view for courses and enrolled course just add an if else statment to check
# wether student is enrolled in that course and render template accorrdingly

# this will be for course details
def course(request,courseId):
    # check if logged in
    #       if not return to login_view
    # check if user is enrolled in course 
    if request.user.is_authenticated:
        user = request.user
        try:
            student = Student.objects.get(user=user)
        except Student.DoesNotExist:        
            return redirect("instructorHome")
        
        course = Course.objects.filter(id = courseId).first()
        if course is None:
            return redirect("home")
        notificationCount = Notification.objects.filter(user  = user ,read = False).count()

        if student in course.students.all():
            assignment  = Assignment.objects.filter(course = course)
            assignments = []
            for a in assignment:
                data = {
                    "a":a,
                    "submission": SubmittedAssignment.objects.filter(assignment = a,student = student).first()

                }
                assignments.append(data)
            # print(assignments)
            return render(request,"student/courseEnrolled.html",
            {
                "course":course,
                "assignments" : assignments,
                "notificationCount":notificationCount

             
            })

        return render(request,"student/course.html",{
            "course":course,
            "notificationCount":notificationCount
})
    else:
        return redirect("login")


