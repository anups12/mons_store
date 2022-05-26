from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer


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
class UpdateCustomer(forms.ModelForm):
    class Meta:
        model = Customer
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