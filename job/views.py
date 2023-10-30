from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
from .form import ApplyJob 
# Create your views here.

def job_list(request):
    job_list=Job.objects.all()
    print("#####################################",job_list)
    # Show 1 contacts per page.
    paginator = Paginator(job_list, 1) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)  

    # context communicate with template 
    context ={
        "joblist": page_obj

    }

    return render(request, 'job/job_list.html',context ) 


def job_details(request, slug):
    only_job = Job.objects.get(slug=slug) # return get 1 response for job but return  filter multi jobs 
    print("###################################################",only_job)
    # if request.method == "POST":
    #     pass
    # else:
    #     form = ApplyJob()
    context={
        "unique_job":only_job,
        "form":form,


    }
    return render(request,"job/job_details.html",context )

