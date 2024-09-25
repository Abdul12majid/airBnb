from django.shortcuts import render, HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Listing
from .serializers import PropSerializer


# Create your views here.
def index(request):
	return HttpResponse("Air BnB")


class properties(ListCreateAPIView):
	queryset = Listing.objects.all()
	serializer_class = PropSerializer