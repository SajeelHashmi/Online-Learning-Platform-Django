from django.urls import path
from . import views
urlpatterns = [

    path('<int:courseId>', views.forum, name='forum'),
    path('newPost', views.newPost, name='newPost'),
    path('newReply', views.newReply, name='newReply'),


]
