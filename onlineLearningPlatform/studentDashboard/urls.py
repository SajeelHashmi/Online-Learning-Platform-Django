from django.urls import path
from . import views
urlpatterns = [

    path('', views.studentHome, name='home'),
    path('offeredcourses', views.offeredcourses, name='offeredcourses'),
    path('course/<int:courseId>', views.course, name='course'),
    path("submitAssignment",views.submitAssignment , name="submitAssignment"),
    path("enrollCourse",views.enrollCourse , name="enrollCourse")

]
