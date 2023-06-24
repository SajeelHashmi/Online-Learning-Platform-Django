from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Instructor)
admin.site.register(Assignment)
admin.site.register(SubmittedAssignment)
admin.site.register(Course)
admin.site.register(Tag)
admin.site.register(AssignedAssignment)

