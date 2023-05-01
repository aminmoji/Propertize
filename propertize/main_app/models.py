from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
PROPERTY_TYPE = (('condo', 'Condominium'),
                 ('house', 'House'),
                 )

class Property(models.Model):
    title = models.CharField(max_length=50, label="Title: ")
    price = models.IntegerField(label="Price: ")
    description = models.CharField(max_length=300, label="Description: ")
    address = models.CharField(max_length=50, label="Adderess: ")
    bedroom = models.IntegerField(label="No. of Bedrooms: ")
    bathroom = models.IntegerField(label="No. of Bathrooms: ")
    sqf = models.IntegerField(label="Area (sqft): ")
    type = models.CharField(choices=PROPERTY_TYPE, default='condo')
    lat = models.IntegerField()
    long = models.IntegerField()
    images = models.ImageField(null=False, blank=False, upload_to="images/")
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return reverse('', kwargs={'property_id': self.id})
    
