from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_user),
    path("register", views.register),
    path("property_booked", views.property_booked),
    path("my_bookings", views.my_bookings),
    path("my_booking_history", views.my_booking_history),
    path("unbook/<int:pk>", views.unbook),

]