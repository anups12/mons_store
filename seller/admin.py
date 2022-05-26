from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Maincategory)
class MaincategoryRegister(admin.ModelAdmin):
    model=Maincategory
    list_display=('name',)

@admin.register(Subcategory)
class SubcategoryRegister(admin.ModelAdmin):
    model=Subcategory
    list_display=('name', 'maincategory')

@admin.register(Brand)
class BrandRegister(admin.ModelAdmin):
    model=Brand
    list_display=('name',)

@admin.register(Seller)
class SellerRegister(admin.ModelAdmin):
    model=Seller
    list_display=('user','name','email','pic')

@admin.register(Product)
class ProductRegister(admin.ModelAdmin):
    model=Product
    list_display=('name','size','maincategory','finalprice')