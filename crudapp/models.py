from django.db import models
# Create your models here.
class Employee (models.Model):
    SNo = models.IntegerField()
    name = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    Address = models.CharField(max_length=80)
    Password = models.CharField(max_length=20)




