from django.db import models
# Create your models here.
class contact(models.Model):
    palce=models.CharField( max_length=50)
    phone=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)