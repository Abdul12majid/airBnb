from django.shortcuts import render, HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Listing, Review, Rating, Booking, Booking_status
from .serializers import PropSerializer, UrlSerializer, RevSerializer, BookingsSerializer, BookSerializer, ReviewSerializer
from rest_framework.pagination import PageNumberPagination
from django.urls import resolve
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import QuerySet
import datetime


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
def reviews(request, pk):
	listing = Listing.objects.get(id=pk)
	guest = request.user
	all_reviews = Review.objects.all()
	serializer_class = RevSerializer(all_reviews, many=True)
	new_review = ReviewSerializer(data=request.data)
	if new_review.is_valid():
		rate_id = request.data['rating']
		rating = Rating.objects.get(id=rate_id)
		comment = request.data['comment']
		user_review = Review.objects.create(
			listing=listing,
			rating=rating,
			guest=guest,
			comment=comment
			)
		user_review.save()

		return Response({'Message':"Thanks for your feedback", 'info':serializer_class.data})
	else:
		return Response({'info':new_review.errors})
	#return Response({serializer_class.data})


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

	#creating reservation
	if serializer.is_valid():
		check_in_date = request.data['check_in_date']
		strp_check_in_date = datetime.datetime.strptime(check_in_date, "%Y-%m-%d")
		check_out_date = request.data['check_out_date']
		strp_check_out_date = datetime.datetime.strptime(check_out_date, "%Y-%m-%d")
		date_diff = strp_check_out_date - strp_check_in_date
		total_price = date_diff.days*listing_price
		create_booking = Booking.objects.create(
				listing=listing,
				guest=guest,
				check_in_date=check_in_date,
				check_out_date=check_out_date,
				total_price=total_price,
				status=status,
				)
		#add booking to user profile
		user_reservation = guest.profile
		user_reservation.bookings_made.add(listing)
		user_reservation.save()

		
		last_booking = guest.profile.bookings_made.latest('id')
		serializer_class = BookingsSerializer(last_booking)
		property_class = PropSerializer()
		context = {
			'info':serializer_class.data, 
			"Property information": property_class.data
			}
		return Response(context)
	else:
		return Response({'info':serializer.errors})
	#return Response({'info': 'book suites', 'info2':'date in format yyyy-mm-dd'})
