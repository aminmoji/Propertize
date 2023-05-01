from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path("about/", views.about, name="about"),
    path("properties/", views.properties_index, name="index"),
    path("properties/create/", views.PropertyCreate.as_view(), name='properties_create')
]