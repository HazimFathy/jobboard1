from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from job.models import Job
# Create your models here.



User = get_user_model()


# profile model 
class Profile(models.Model):
    jobs = models.ManyToManyField(Job, related_name="profiles", blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city =models.CharField(default='tanta',max_length=100)
    country = models.CharField(default='Egypt',max_length=100)
    image = models.ImageField(upload_to='acc/')
    number = PhoneNumberField(default='+201234567891',max_length=30)
    
    
    def __str__(self):
        return str(self.user.get_full_name)
    
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    
    




