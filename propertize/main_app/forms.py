from django.forms import ModelForm
from .models import Property, CustomUser, Showing
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

PROPERTY_TYPE = (('condo', 'Condominium'),
                 ('house', 'House'),
                 )


class PropertyForm(ModelForm):
   type = forms.ChoiceField(choices=PROPERTY_TYPE, label='Type of Property')
  
   class Meta:
        model = Property
        fields = ('title', 'price', 'description', 'address', 'bedroom', 'bathroom', 'sqf', 'type', 'images')
        labels = {
        'title': 'Title', 'price': 'Price', 'description': 'Description', 'address': 'Address', 'bedroom': 'No. of Bedrooms', 'bathroom': 'No. of Bathrooms', 'sqf': 'Area (sqft):', 'type': 'Type of Property', 'images': ''
        }
        widgets = {
        'type': forms.Select(attrs={'class': 'form-control'})
        }

class ShowingForm(ModelForm):
   class Meta:
      model = Showing
      fields = ("date",)


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

