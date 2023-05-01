from django.forms import ModelForm
from .models import Property

class PropertyForm(ModelForm):
  class Meta:
    model = Property
    fields = ('title', 'price', 'description', 'address', 'bedroom', 'bathroom', 'sqf', 'type', 'lat', 'long', 'images')
    