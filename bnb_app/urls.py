from django.urls import path
from . import views

urlpatterns = [
   
    path("", views.index),
    path("properties", views.properties.as_view()),
    path("property/<int:pk>", views.property_info.as_view()),
    path("reviews/<int:pk>", views.reviews),
    path("bookings", views.bookings.as_view()),
    path("book/<int:pk>", views.book),
    path("booked_property", views.booked_property),
    path("booking_history", views.booking_history),
    path("search/<int:pk>", views.search)


]