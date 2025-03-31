from django.db import models

# Create your models here
class Post(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=12)
    content=models.TextField()
class Comment(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    title=models.CharField(max_length=12)
    coment=models.TextField()

 
