from django.contrib import admin
from .models import *
# Register your models here.
class studData(admin.ModelAdmin):
    list_display=['id','name','city']
admin.site.register(stdinfo,studData)