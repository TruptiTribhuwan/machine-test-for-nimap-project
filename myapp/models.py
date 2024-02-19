from django.db import models

# Create your models here.
class client(models.Model):
    roll=models.CharField(max_length=45)
    name=models.CharField(max_length=45)
    createdby=models.CharField(max_length=45)
    Project=models.CharField(max_length=45)

class User(models.Model):
    uname=models.CharField(max_length=45)
