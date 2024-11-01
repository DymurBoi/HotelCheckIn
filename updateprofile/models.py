from django.db import models

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255,null=True,blank=True)
    email= models.CharField(max_length=255, null=True,blank=True)
    phone_num= models.CharField(max_length=11,null=True,blank=True)
    password=models.CharField(max_length=150,null=True,blank=True)
    profile_pic=models.ImageField(default='default_profile.jpg',blank=True)
    
    def __str__(self):
        return self.name