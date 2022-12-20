from django.db import models
from django.urls import reverse
# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=50)
    FatherName=models.CharField(max_length=50)
    ClassName=models.IntegerField()
    Contact=models.IntegerField()

class Teacher(models.Model):
    Name=models.CharField(max_length=50)
    exp=models.IntegerField()
    subject=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('listteachers')