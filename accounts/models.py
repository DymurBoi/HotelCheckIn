from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)  # Hash the password before saving
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    username = models.EmailField(max_length=150, unique=True)
    firstname = models.CharField(max_length=30, default='')
    lastname = models.CharField(max_length=30, default='')
    phone_number = models.CharField(max_length=15, default='')  
    address= models.CharField(max_length=200, default='')  
    # Add the password field explicitly
    password = models.CharField(max_length=128, null=False)
    profile_pic=models.ImageField(default='default_profile.jpg',blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['firstname', 'lastname', 'phone_number']

    def __str__(self):
        return self.username
