from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product, Seller

class ProductAdd(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude=['seller']
        choices_field = [
            ('In Stock ','In Stock '),
            ('Out of  Stock ','Out of  Stock '),
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Your Name'}),
            'maincategory': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Your Email'}),
            'finalprice': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'final Price'}),
            'baseprice': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Base Price'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control','placeholder': ' Discount'}),
            'size': forms.Select(attrs={'class': 'form-control'}),
            'color': forms.Select(attrs={'class': 'form-control'}),
            'subcategory': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.RadioSelect(choices=choices_field),  
            'pic1':forms.FileInput(attrs={'class':'form-control'})  ,
            'pic2':forms.FileInput(attrs={'class':'form-control'}) , 
            'pic3':forms.FileInput(attrs={'class':'form-control'})  ,
            'pic4':forms.FileInput(attrs={'class':'form-control'})  ,
         }

class UserCreate(UserCreationForm):
    class Meta:
        model = User
        fields=('username', 'email', 'password1', 'password2')
        widget={
            'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Unique username'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Email'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Password '}),
            'password2':forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}),
        }
class UpdateSeller(forms.ModelForm):
    class Meta:
        model = Seller
        fields='__all__'
        exclude = ['user']
        widget={
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter name'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Email'}),
            'phone':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Enter Phone Number '}),
            'address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
            'pin':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Pincode'}),
            'city':forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}),
            'state':forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}),
        }