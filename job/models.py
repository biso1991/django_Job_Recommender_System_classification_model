from django.db import models
import uuid
import os
from django.utils.text import slugify
# # Create your models here.
'''django model field
    -html widget
    -validation 'email or not'
    -db size 'char, textor time ... best field for database'

'''



class Categorys(models.Model):
      name = models.CharField(max_length=20)

      def __str__(self):
        return self.name 
      

# set images in media file  by id  
def upload_image(instance, filename):
    imagename, extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id , extension)

JOB_TYPE=(
    ('Full Time', 'Full time' ),
    ('Part Time', 'Part Time'),
)
class Job(models.Model):# jobs table 
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title= models.CharField(max_length=30)# column
    # location
    job_type = models.CharField(max_length=50,choices=JOB_TYPE)
    descriptions= models.TextField(max_length=1000)
    published_add = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary =  models.IntegerField(default=0)
    experiences = models.IntegerField(default=0)
    catagorys = models.ForeignKey(Categorys, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = upload_image) 
    slug= models.SlugField(blank=True, null=True)

    
    def save (self, *args, **kwargs) :
        self.slug = slugify(self.title)
        super(Job, self).save(*args,**kwargs)   # 
    
    
    def __str__(self):
        return self.title

class User_apply_job(models.Model): 
    apply = models.ForeignKey("Job", verbose_name=("appl_job"), on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email=models.EmailField( max_length=50)
    website = models.URLField()
    cv = models.FileField( upload_to="cv/", max_length=100)
    coverletter = models.TextField(max_length=3000)
    create_at = models.DateField( auto_now=True)
    
    def __str__(self):
        return self.name
