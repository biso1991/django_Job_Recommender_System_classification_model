from django.contrib import admin

# Register your models here.

from .models import Job, Categorys, User_apply_job

admin.site.register(Job)
admin.site.register(Categorys)
admin.site.register(User_apply_job)
