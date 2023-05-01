from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Property(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=300)
    address = models.CharField(max_length=50)
    bedroom = models.IntegerField()
    bathroom = models.IntegerField()
    sqf = models.IntegerField()
    type = models.CharField()
    lat = models.IntegerField()
    long = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.title}'
    def get_absolute_url(self):
        return reverse('', kwargs={'property_id': self.id})
    

