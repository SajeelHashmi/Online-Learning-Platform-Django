from django.urls import path
from . import views
urlpatterns = [

    path('', views.instructorHome, name='instructorHome'),
    path('newcourse', views.newCourse, name='newCourse'),
    path('course/<int:courseId>', views.courseDashboard, name='courseDashboard'),
    path('newAssignment', views.newAssignment, name='newAssignment'),
    path('viewSubmissions/<int:assignmentId>', views.viewSubmissions, name='viewSubmissions'),



]
