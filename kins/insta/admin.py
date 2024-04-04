from django.contrib import admin
from . models import *
# Register your models here.
@admin.register(User)
class add(admin.ModelAdmin):
    list_display=['username','email', "is_staff", "is_active"]

@admin.register(course)
class dept(admin.ModelAdmin):
    list_display=['name','description','creation_date','user']