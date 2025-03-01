from django_countries.fields import CountryField
from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model


User = get_user_model()

JOB_TYPE=(
  ('FULL TIME','FULL TIME'),
  ('PART TIME','PART TIME'),
)



# Create your models here.
#job's class
class Job(models.Model):
    
    owner=models.ForeignKey(User, on_delete=models.CASCADE , related_name='jobs')
    title=models.CharField(max_length=30)
    country = models.CharField (max_length=80 , default= 'EGYPT')
    city = models.CharField (max_length=80 , default= 'Tanta')
    description=models.TextField(max_length=10000)
    Published_on=models.DateTimeField( auto_now=True)
    vacancy=models.IntegerField(default=1)
    Salary =models.IntegerField(default=1)
    Job_Nature=models.CharField(max_length=50,choices=JOB_TYPE)
    category =models.ForeignKey('category',on_delete=models.CASCADE)
    image = models.ImageField( upload_to='jobs/')
    slug = models.SlugField(blank=True, null=True, unique=True)  

   
    def __str__ (self):
        return self.title
      
    def save(self, *args, **kwargs):
        if self.pk:
            existing = Job.objects.filter(pk=self.pk).first()
            if existing and not self.image:
                self.image = existing.image 
                
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            count = 0
            while Job.objects.filter(slug=slug).exists():
                count += 1
                slug = f"{base_slug}-{count}"
            self.slug = slug
        super().save(*args, **kwargs)
        

#job's category class
class category(models.Model):
    title=models.CharField( max_length=50)
    def __str__(self) :
        return self.title

#apply form class
class apply(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    job=models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)
    name=models.CharField( max_length=50)
    email=models.EmailField(max_length=254)
    website=models.URLField(max_length=200)
    cv=models.FileField(upload_to='apply/')
    coverletter=models.TextField(max_length=1000)
    
    def __str__ (self):
        return self.name
    
    
    
    
    
    

 
