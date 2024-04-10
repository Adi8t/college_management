from django.contrib import admin
from . models import *
# Register your models here.
@admin.register(User)
class add(admin.ModelAdmin):
    list_display=['username','email', "is_staff", "is_active","is_superuser"]
@admin.register(SubjectDetails)
class sub(admin.ModelAdmin):
    list_display=['subject_id','subject','subject_code','teacher']
