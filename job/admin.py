from django.contrib import admin

# Register your models here.

from .models import job, Categorys

admin.site.register(job)
admin.site.register(Categorys)
