from django.db import models

# Create your models here.
'''django model field
    -html widget
    -validation 'email or not'
    -db size 'char, textor time ... best field for database'

'''



class Categorys(models.Model):
      name = models.CharField(max_length=20)

      def __str__(self):
        return self.name 
      



JOB_TYPE=(
    ('Full Time', 'Full time' ),
    ('Part Time', 'Part Time'),
)
class job(models.Model):# table job
    title= models.CharField(max_length=30)# column
    # location
    job_type = models.CharField(max_length=50,choices=JOB_TYPE)
    descriptions= models.TextField(max_length=1000)
    published_add = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary =  models.IntegerField(default=0)
    experiences = models.IntegerField(default=0)
    catagorys = models.ForeignKey(Categorys, on_delete=models.CASCADE)
    # 
    def __str__(self):
        return self.title

