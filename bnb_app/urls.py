from django.urls import path
from . import views

urlpatterns = [
   
    path("", views.index),
    path("properties", views.properties.as_view()),
]