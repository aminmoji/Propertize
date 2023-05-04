from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path("about/", views.about, name="about"),
    path("index/", views.properties_index, name="index"),
    path('index/<int:property_id>', views.property_detail, name='detail'),
    path("properties/create/", views.add_property, name='add_property'),
    path('properties/<int:pk>/update/', views.PropertyUpdate.as_view(), name='property_update'),
    path('properties/<int:pk>/delete/', views.PropertyDelete.as_view(), name='property_delete'),
    path('properties/index/<int:property_id>/add_showing/', views.add_showing, name='add_showing'),
    path('properties/showings', views.showing_list, name='showing_list'),
    path('properties/<int:property_id>/add_to_favorites/', views.add_to_favorites, name='add_to_favorites'),
    path('properties/favorites', views.favorites_list, name='favorites_list'),
    path('<int:favorite_id>/delete/', views.delete_from_favorites, name='delete_from_favorites'),
    path("signup/",  views.SignUpView.as_view(), name="signup"),
]