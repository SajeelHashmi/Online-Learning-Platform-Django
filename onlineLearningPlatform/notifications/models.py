from django.db import models
from instructorDashboard.models import Course,Assignment
from forums.models import Forum,Post
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.


# create 2 models one for course related notification
# assignment uploaded assessment marked etc
# other for forum related notifications#

class Notification(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE,null=True,blank=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    content = models.TextField()
    timeStamp = models.DateTimeField()
    def __str__(self) -> str:
        return self.user.username +" : " + self.content


