from django.contrib import admin
from .models import *

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['id','createdat','title','content']

admin.site.register(Post)
admin.site.register(Comment)