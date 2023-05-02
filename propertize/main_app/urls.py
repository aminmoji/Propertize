from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name="home"),
    path("about/", views.about, name="about"),
    path("properties/", views.properties_index, name="index"),
    path('properties/<int:property_id>', views.property_detail, name='detail'),
    path("properties/create/", views.PropertyCreate.as_view(), name='property_create'),
    path('properties/<int:pk>/update/', views.PropertyUpdate.as_view(), name='property_update'),
    path('properties/<int:pk>/delete/', views.PropertyDelete.as_view(), name='property_delete'),
    path("properties/<int:property_id>/showing/create", views.add_showing, name='add_showing')
]