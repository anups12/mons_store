from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from seller.models import Product

# Create your models here.


class Customer(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100,default=None,null=True,blank=True)
    pin = models.CharField(max_length=50,default=None,null=True,blank=True)
    city = models.CharField(max_length=50,default=None,null=True,blank=True)
    state = models.CharField(max_length=50,default=None,null=True,blank=True)
    pic = models.ImageField(upload_to='images',default='avatar.jpg',null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.name)



class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now_add=True)
    trans_id = models.CharField(max_length=100, null=True)
    
    def __str__(self) :
        return str(self.id)

    @property
    def Total_price(self):
        product = self.orderitem_set.all()
        total = sum([item.get_total for item in product])
        return total

    @property
    def Total_quantity(self):
        product=self.orderitem_set.all()
        total = sum([item.quantity for item in product])
        return total

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True )
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return str(self.order)

    @property
    def get_total(self):
        total = self.product.finalprice*self.quantity
        return total

class Shipping(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True )
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True )
    name=models.CharField(max_length=100, null=True)
    phone = models.IntegerField(null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    pincode = models.CharField(max_length=100, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return str(self.customer)

class Wishlist(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True )
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.product)
    
class ContactForm(models.Model):
    name=models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    subject=models.CharField(max_length=100)
    description=models.TextField(max_length=1000)

    def __str__(self):
        return self.name
    