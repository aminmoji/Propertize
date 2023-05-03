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
    username = models.CharField(unique=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name}'s username is {self.username}"


class Property(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=300)
    address = models.CharField(max_length=50)
    bedroom = models.IntegerField()
    bathroom = models.IntegerField()
    sqf = models.IntegerField()
    type = models.CharField(max_length=15, choices=PROPERTY_TYPE, default=PROPERTY_TYPE[0][0])
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

