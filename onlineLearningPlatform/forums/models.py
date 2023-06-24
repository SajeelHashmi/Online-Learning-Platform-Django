from django.db import models
from instructorDashboard.models import Course
from django.contrib.auth.models import User


# Create your models here.
class Forum(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.course.title + " Forum"

class Post(models.Model):
    forum = models.ForeignKey(Forum,on_delete=models.CASCADE)
    title = models.TextField()
    uploadTime =  models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    def __str__(self) -> str:
        return "Title: " + self.title + " Author: " + self.author.username 

class Reply(models.Model):
    post = models.ForeignKey(Post , on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    uploadTime =  models.DateTimeField()

    def __str__(self) -> str:
        return "Post: " + self.post.title + " Author: " + self.author.username 

