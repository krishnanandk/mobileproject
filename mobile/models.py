from django.db import models

# Create your models here.
from django.db import models




class Brands(models.Model):
    brand_name=models.CharField(max_length=150)

    def __str__(self):
        return self.brand_name


class Product(models.Model):
    mobile_name=models.CharField(max_length=120,unique=True)
    brand=models.ForeignKey(Brands,on_delete=models.CASCADE)
    price=models.IntegerField()
    specs=models.CharField(max_length=200)
    image=models.ImageField(upload_to="images")

    def __str__(self):
        return self.mobile_name