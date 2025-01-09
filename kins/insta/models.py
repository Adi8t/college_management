from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import MyUserManager


from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    joining_date = models.DateTimeField(null=True,blank=True)
    subject = models.CharField(max_length=100,null=True)
    DAY_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    )
    ROLES = (
        ("principal", 'Principal'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    department=(
        ("EC","EC"),
        ("IT","IT"),
        ("COMPUTER","COMPUTER"),
    )

    day = models.CharField(max_length=10, choices=DAY_CHOICES, null=True)
    role = models.CharField(max_length=100, choices=ROLES,default="student")
    dept=models.CharField(max_length=100,choices=department,default="EC")
    is_staff = models.BooleanField(default=True)  
    is_active = models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=True)
    
    objects = MyUserManager()

  
    USERNAME_FIELD = "email"
    
    REQUIRED_FIELDS = []

class SubjectDetails(models.Model):
    subject_id = models.AutoField(primary_key=True,null=False)
    subject = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=100)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='subjects_taught')
   

    class Meta:
        db_table = 'subject_details'
