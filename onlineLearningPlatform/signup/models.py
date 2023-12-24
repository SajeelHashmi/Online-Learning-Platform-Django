from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='student_pfp/', blank=True, null=True)
    id = models.AutoField(primary_key=True)
    def __str__(self) -> str:
        return self.user.username