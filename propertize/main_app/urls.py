from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.home, name="home"),
    path("about/", views.about, name="about"),
    path("properties/", views.properties_index, name="index"),
    path('properties/<int:property_id>', views.property_detail, name='detail'),
    path("properties/create/", views.PropertyCreate.as_view(), name='add_property'),
    path('properties/<int:pk>/update/', views.PropertyUpdate.as_view(), name='property_update'),
    path('properties/<int:pk>/delete/', views.PropertyDelete.as_view(), name='property_delete'),
]