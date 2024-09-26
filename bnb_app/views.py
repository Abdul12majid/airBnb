from django.shortcuts import render, HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Listing, Review, Rating, Booking, Booking_status
from .serializers import PropSerializer, UrlSerializer, RevSerializer, BookSerializer, BookaSerializer
from rest_framework.pagination import PageNumberPagination
from django.urls import resolve
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import QuerySet


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
	queryset = Listing.objects.filter(is_available=True)
	pagination_class = PageNumberPagination
	serializer_class = PropSerializer


class property_info(RetrieveUpdateDestroyAPIView):
	queryset = Listing.objects.all()
	serializer_class = PropSerializer


class reviews(ListCreateAPIView):
	queryset = Review.objects.all()
	pagination_class = PageNumberPagination
	serializer_class = RevSerializer


class book(ListCreateAPIView):
	queryset = Booking.objects.all()
	pagination_class = PageNumberPagination
	serializer_class = BookSerializer

@api_view(['POST', 'GET'])
def book_a(request, pk):
	serializer = BookaSerializer(data=request.data)
	listing = Listing.objects.get(id=pk)
	guest = request.user
	listing_price = listing.price_per_night
	status = Booking_status.objects.get(id=1)
	if serializer.is_valid():
		check_in_date = request.data['check_in_date']
		check_out_date = request.data['check_out_date']
		date_diff = check_out_date - check_in_date
		total_price = date_diff*listing_price
		create_booking = Booking.objects.create(
				listing=listing,
				guest=guest,
				check_in_date=check_in_date,
				check_out_date=check_out_date,
				total_price=total_price,
				status=status,
				)

		return Response({'info':serializer.data})
	else:
		return Response({'info':serializer.errors})
	return Response({'info': 'book suites', 'info2':'date in format yyyy-mm-dd'})





