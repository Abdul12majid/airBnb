from django.shortcuts import render, HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Listing, Review, Rating, Booking, Booking_status
from .serializers import PropSerializer, UrlSerializer, RevSerializer, BookingsSerializer, BookSerializer
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


@api_view(['POST', 'GET'])
def reviews(request):
	all_reviews = Review.objects.all()
	serializer_class = RevSerializer(all_reviews, many=True)
	new_review = RevSerializer(data=request.data)
	if new_review.is_valid():
		prop_id = request.data['listing']
		listing = Listing.objects.get(id=prop_id)
		rate_id = request.data['rating']
		rating = Rating.objects.get(id=rate_id)
		guest = request.user
		comment = request.data['comment']
		user_review = Review.objects.create(
			listing=listing,
			rating=rating,
			guest=guest,
			comment=comment
			)
		user_review.save()

		return Response({'Message':"Thanks for your feedback", 'info':new_review.data})
	else:
		return Response({'info':serializer_class.data})




class bookings(ListCreateAPIView):
	queryset = Booking.objects.all()
	pagination_class = PageNumberPagination
	serializer_class = BookingsSerializer

@api_view(['POST', 'GET'])
def book(request, pk):
	serializer = BookSerializer(data=request.data)
	listing = Listing.objects.get(id=pk)
	guest = request.user
	listing_price = listing.price_per_night
	status = Booking_status.objects.get(id=1)
	if serializer.is_valid():
		check_in_date = request.data['check_in_date']
		check_out_date = request.data['check_out_date']
		date_diff = int(check_out_date - check_in_date)
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
	#return Response({'info': 'book suites', 'info2':'date in format yyyy-mm-dd'})



#list and tuples and dictionaries manipulations


