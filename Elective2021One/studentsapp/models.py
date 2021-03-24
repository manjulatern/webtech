from django.db import models

# Create your models here.
class Student(models.Model):
	full_name =  models.CharField(max_length=200)
	roll_number =  models.IntegerField()
	address = models.CharField(max_length=200)