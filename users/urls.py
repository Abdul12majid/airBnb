from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_user),
    path("register", views.register),
    path("property_booked", views.property_booked),
    path("my_bookings", views.my_bookings),
    path("unbook/<int:pk>", views.unbook),

]