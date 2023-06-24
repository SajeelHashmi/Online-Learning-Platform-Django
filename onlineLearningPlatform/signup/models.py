from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# change models make a student model and an instructor model

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='student_pfp/', blank=True, null=True)
    id = models.AutoField(primary_key=True)
    def __str__(self) -> str:
        return self.user.username