from django.forms import ModelForm
from .models import Property, CustomUser, Showing
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.widgets import DateInput, TimeInput


class PropertyForm(ModelForm):
   class Meta:
        model = Property
        fields = ['title', 'price', 'description', 'address', 'bedroom', 'bathroom', 'sqf', 'type', 'images']
        labels = {
        'title': 'Title', 'price': 'Price', 'description': 'Description', 'address': 'Address', 'bedroom': 'No. of Bedrooms', 'bathroom': 'No. of Bathrooms', 'sqf': 'Area (sqft):', 'type': 'Type of Property', 'images': ''
        }



class ShowingForm(ModelForm):
   print("showing form")
   class Meta:
      model = Showing
      fields = ['date', 'time']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "username", "email", "phone")
        labels = {
           'first_name': 'First Name',
           'last_name': 'Last Name',
           'username': 'Username',
           'email': 'Email',
           'phone': 'Phone No.'
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "password", "email", "phone")

