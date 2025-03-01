from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_delete
# Create your models here.
User = get_user_model()

class Blog (models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='blogs/')
    title= models.CharField (max_length=100)
    description =models.TextField(max_length=1000)
    create_at=models.DateTimeField( auto_now=True)
    category=models.ForeignKey('category',  on_delete=models.CASCADE)
    active =models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title
# delete the image of the blog if the blog deleted   
@receiver(post_delete, sender=Blog)
def delete_post_image(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):  
            os.remove(instance.image.path) 
    
    
    
class Comment(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    write_a_comment=models.TextField(max_length=10000)
    created_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
    
        
    



    
    

    

    
    

   
    
    
    
   
class Category(models.Model):
    title=models.CharField( max_length=50)
    def __str__(self):
        return self.title
