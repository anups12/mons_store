from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Customer)
class CustomerRegister(admin.ModelAdmin):
    model=Customer
    list_display=('user','name', 'email', 'phone', 'pic')

@admin.register(Order)
class OrderRegister(admin.ModelAdmin):
    model=Order
    list_display=('customer',)

@admin.register(OrderItem)
class OrderItemRegister(admin.ModelAdmin):
    model=OrderItem
    list_display=('product','order','quantity')

@admin.register(Shipping)
class ShippingRegister(admin.ModelAdmin):
    model=Shipping
    list_display=('customer','order','address')

@admin.register(Wishlist)
class ShippingRegister(admin.ModelAdmin):
    model=Wishlist
    list_display=('id','product','customer')

@admin.register(ContactForm)
class ShippingRegister(admin.ModelAdmin):
    model=ContactForm
    list_display=('id','name','email', 'phone', 'subject')