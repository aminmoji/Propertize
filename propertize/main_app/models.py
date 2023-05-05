from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
import datetime



# Create your models here.
PROPERTY_TYPE = (('condo', 'Condominium'),
                 ('house', 'House'),
                 )


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=25)
    username = models.CharField(unique=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    favorites = models.ManyToManyField('Property', related_name='favorited_by')

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
    type = models.CharField(choices=PROPERTY_TYPE, default='condo', max_length=10, label="Type: ", widget=models.Select(choices=PROPERTY_TYPE))
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=300)
    address = models.CharField(max_length=50)
    bedroom = models.IntegerField()
    bathroom = models.IntegerField()
    sqf = models.IntegerField()
    type = models.CharField(choices=PROPERTY_TYPE, default='condo', max_length=10)
    images = models.ImageField(null=False, blank=False, upload_to="images/")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'property_id': self.id})
    

class Showing(models.Model):
    date = models.DateField(('showing date'), default=datetime.date.today())
    time = models.TimeField(('showing time'), default=datetime.time(hour=12, minute=0))
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'The open house is set for the date of {self.date} for {self.property} by {self.user}'

    def get_absolute_url(self):
        return reverse('property_detail)', kwargs={'pk': self.id})

    class Meta:
     ordering = ['-date']


class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
