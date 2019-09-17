from django.db import models


# Create your models here.

class Employee(models.Model):
    empname = models.CharField(max_length=30)
    salary = models.IntegerField(default=1000)
    designation = models.CharField(max_length=30)
    gender = models.CharField(max_length=3)


