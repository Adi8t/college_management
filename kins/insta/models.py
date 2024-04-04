from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import MyUserManager


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    joining_date = models.DateTimeField(auto_now_add=True)
    
   
    ROLES = (
        (1, 'Principal'),
        (2, 'Teacher'),
        (3, 'Student'),
    )
   
    role = models.CharField(max_length=100, choices=ROLES,default=1)
    is_staff = models.BooleanField(default=True)  
    is_active = models.BooleanField(default=True)
    
    
    objects = MyUserManager()

  
    USERNAME_FIELD = "email"
    
    REQUIRED_FIELDS = []

class course(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(null=True)
    creation_date=models.DateField(auto_now_add=True)
    user=models.OneToOneField(User,on_delete=models.DO_NOTHING,null=True,blank=True)



