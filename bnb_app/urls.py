from django.urls import path
from . import views

urlpatterns = [
   
    path("", views.index),
    path("properties", views.properties.as_view()),
    path("property/<int:pk>", views.property_info.as_view()),
    path("reviews", views.reviews.as_view()),
    path("bookings", views.bookings.as_view()),
    path("book/<int:pk>", views.book)


]