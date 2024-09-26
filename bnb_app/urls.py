from django.urls import path
from . import views

urlpatterns = [
   
    path("", views.index),
    path("properties", views.properties.as_view()),
    path("property/<int:pk>", views.property_info.as_view()),
    path("reviews", views.reviews.as_view()),
    path("book", views.book.as_view()),
    path("book_a/<int:pk>", views.book_a)


]