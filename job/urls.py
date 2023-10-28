
from django.urls import include, path
from . import views
#name app for created
app_name='job'

urlpatterns = [
    path('',views.job_list),
    path('<str:slug>',views.job_details, name="job_details"),
    
]