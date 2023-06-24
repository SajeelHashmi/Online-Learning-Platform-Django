from django.contrib import admin
from .models import Post,Reply,Forum
# Register your models here.


admin.site.register(Forum)
admin.site.register(Post)
admin.site.register(Reply)
