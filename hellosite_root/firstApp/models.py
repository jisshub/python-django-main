from django.db import models


# Create your models here.

class Employee(models.Model):
    empname = models.CharField(max_length=30)
    salary = models.IntegerField(default=1000)
    designation = models.CharField(max_length=30)
    gender = models.CharField(max_length=3)

    def __str__(self):
        return self.empname


# class Course(models.Model):
#     course = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.course
#
#
# class Trainer(models.Model):
#     name = models.CharField(max_length=30)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
