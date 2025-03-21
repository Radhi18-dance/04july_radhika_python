from django.db import models

# Create your models here.
class signmodel(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    fullname=models.CharField(max_length=20)
    email=models.EmailField()
    mobile=models.BigIntegerField()
    password=models.CharField(max_length=12)

class event(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    zip=models.BigIntegerField()
    email=models.EmailField()
    
class save(models.Model):
    fullname=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.BigIntegerField()
    address=models.TextField()




  