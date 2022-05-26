from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Maincategory(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    maincategory = models.ForeignKey(Maincategory, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100,default=None,null=True,blank=True)
    pin = models.CharField(max_length=50,default=None,null=True,blank=True)
    city = models.CharField(max_length=50,default=None,null=True,blank=True)
    state = models.CharField(max_length=50,default=None,null=True,blank=True)
    pic = models.FileField(upload_to='images',default='avatar.jpg',null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    field_size=(
        ('s','s'),
        ('m','m'),
        ('l','l'),
        ('xl','xl'),
    )
    color_choice=(
        ('red','red'),
        ('blue','blue'),
        ('green','green'),
        ('pink','pink'),
        ('black','black'),
        ('brown','brown'),
        ('yellow','yellow'),
        ('white','white'),
        ('silver','silver'),
    )
    name = models.CharField(max_length=120)
    maincategory = models.ForeignKey(Maincategory,on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE, null=True)
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE,default=None)
    baseprice = models.IntegerField()
    discount = models.IntegerField()
    finalprice = models.IntegerField()
    size = models.CharField(max_length=10, choices=field_size, default='s', null=True, blank=True)
    color = models.CharField(max_length=20, choices=color_choice, null=True)
    description = models.TextField()
    stock = models.CharField(max_length=20,default="In Stock")
    pic1 = models.ImageField(upload_to="images")
    pic2 = models.ImageField(upload_to="images",default=None,null=True,blank=True)
    pic3 = models.ImageField(upload_to="images",default=None,null=True,blank=True)
    pic4 = models.ImageField(upload_to="images",default=None,null=True,blank=True)

    def __str__(self):
        return self.name
    
