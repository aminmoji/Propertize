from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


# Create your models here.
PROPERTY_TYPE = (('condo', 'Condominium'),
                 ('house', 'House'),
                 )


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=25)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=14)
    email = models.EmailField()
    phone = models.IntegerField()

    def __str__(self):
        return f"{self.first_name}'s username is {self.username}"


class Property(models.Model):
    title = models.CharField(max_length=50, label="Title: ")
    price = models.IntegerField(label="Price: ")
    description = models.CharField(max_length=300, label="Description: ")
    address = models.CharField(max_length=50, label="Adderess: ")
    bedroom = models.IntegerField(label="No. of Bedrooms: ")
    bathroom = models.IntegerField(label="No. of Bathrooms: ")
    sqf = models.IntegerField(label="Area (sqft): ")
    type = models.CharField(choices=PROPERTY_TYPE, default='condo')
    images = models.ImageField(null=False, blank=False, upload_to="images/")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return reverse('', kwargs={'property_id': self.id})
    

class Showing(models.Model):
    date = models.DateTimeField('showing date')
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'The open house is set for the date of {self.date} for {self.property} by {self.user}'

    def get_absolute_url(self):
        return reverse('property_detail)', kwargs={'pk': self.id})

    class Meta:
     ordering = ['-date']

