from django.forms import ModelForm
from .models import Property, CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class PropertyForm(ModelForm):
  class Meta:
    model = Property
    fields = ('title', 'price', 'description', 'address', 'bedroom', 'bathroom', 'sqf', 'type', 'lat', 'long', 'images')
    

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "username", "password", "email", "phone")
        labels = {
           'first_name': 'First Name',
           'last_name': 'Last Name',
           'username': 'Username',
           'password': 'Password',
           'email': 'Email',
           'phone': 'Phone No.'
        }

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "password", "email", "phone")