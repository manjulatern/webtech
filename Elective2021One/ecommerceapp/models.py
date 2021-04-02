from django.db import models

from django.contrib.auth.models import User
# Create your models here.

# Product
class Product(models.Model):

	product_name =  models.CharField(max_length=200,default="")
	product_code = models.CharField(max_length=200,default="")
	price = models.IntegerField()
	image = models.CharField(max_length=200,default="")
	units = models.IntegerField()


# UserProduct
class UserProduct(models.Model):
	
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	status = models.IntegerField()
