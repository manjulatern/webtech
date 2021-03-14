from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=100)
	roll_number = models.IntegerField()
	address = models.CharField(max_length=100)
	faculty = models.CharField(max_length=100)