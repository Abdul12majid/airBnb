from django.shortcuts import render, HttpResponse
from django.contrib.auth import login, logout, authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer, SignUpSerializer
from django.contrib.auth.models import User
from bnb_app.serializers import PropSerializer, BookingsSerializer
from bnb_app.models import Booking, Listing
from .models import UserBooking

# Create your views here.

@api_view(['POST', "GET"])
def login_user(request):
	serializer = LoginSerializer(data=request.data)
	if serializer.is_valid():
		username = request.data['username']
		password = request.data['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return Response({'Info': 'Login Successful'})
		else:
			return Response({'Info': 'Incorrect username or password'})

	return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET'])	
def register(request):
	serializer = SignUpSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		response = {
			"info":"Registeration successful",
			"data":serializer.data
		}
		return Response(data=response, status=status.HTTP_201_CREATED)
	return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def property_booked(request):
	user = request.user
	if user.profile.bookings_made.all().count() != 0:
		all_bookings = user.profile.bookings_made.all()
		property_class = PropSerializer(all_bookings, many=True)
		return Response({"info":property_class.data})
	return Response({"info":"No property booked."}) 


@api_view(['GET'])
def my_bookings(request):
	user = request.user
	if UserBooking.objects.filter(guest=user).all().count() != 0:
		user_booking = UserBooking.objects.filter(guest=user).all()
		serializer_class = BookingsSerializer(user_booking, many=True)
		return Response({"info":serializer_class.data})
	return Response({"info":"All bookings cleared."})



@api_view(['GET'])
def unbook(request, pk):
	user = request.user

	#get property
	get_prop = Listing.objects.get(id=pk)
	serializer = PropSerializer(get_prop, many=False)

	#remove from profile
	user_profile = user.profile
	if get_prop in user_profile.bookings_made.all():
		user_profile.bookings_made.remove(get_prop)
		user_profile.book_count -= 1
		user_profile.save()

		#remove from booking model
		booking_prop = UserBooking.objects.get(listing=get_prop)
		booking_prop.delete()
		print('Successfully deleted')

		#turn prop availability
		get_prop.is_available = True
		get_prop.save()
		return Response({"Unbooked":serializer.data})

	return Response({"Unbooked":"Booking not made yet."})


@api_view(['GET'])
def my_booking_history(request):
	user = request.user
	if Booking.objects.filter(guest=user).all().count() != 0:
		user_bookings = Booking.objects.filter(guest=user).all()
		serializer_class = BookingsSerializer(user_bookings, many=True)
		return Response({"info":serializer_class.data})
	return Response({"info":"You have no history."})