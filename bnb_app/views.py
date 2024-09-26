from django.shortcuts import render, HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Listing, Review
from .serializers import PropSerializer, UrlSerializer, RevSerializer
from rest_framework.pagination import PageNumberPagination
from django.urls import resolve
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
#def index(request):
	#return HttpResponse("Air BnB")

@api_view(['POST', 'GET'])
def index(request):
    url_patterns = resolve('bnb_app:home').url_patterns
    endpoint_list = []
    for pattern in url_patterns:
        endpoint = pattern.pattern._regex
        endpoint_list.append(endpoint)
        serializer = UrlSerializer(endpoint_list, many=True)
    return Response({'endpoints':serializer.data})


class properties(ListCreateAPIView):
	queryset = Listing.objects.all()
	pagination_class = PageNumberPagination
	serializer_class = PropSerializer


class property_info(RetrieveUpdateDestroyAPIView):
	queryset = Listing.objects.all()
	serializer_class = PropSerializer


class reviews(ListCreateAPIView):
	queryset = Review.objects.all()
	pagination_class = PageNumberPagination
	serializer_class = PropSerializer