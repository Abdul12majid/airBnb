from django.shortcuts import render, HttpResponse
from django.contrib.auth import login, logout, authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer, SignUpSerializer
from django.contrib.auth.models import User
from bnb_app.serializers import PropSerializer, BookingsSerializer
from bnb_app.models import Booking

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


@api_view(['POST', 'GET'])
def my_bookings(request):
	user = request.user
	if Booking.objects.filter(guest=user).all().count() != 0:
		user_booking = Booking.objects.filter(guest=user).all()
		serializer_class = BookingsSerializer(user_booking, many=True)
		return Response({"info":serializer_class.data})
	return Response({"info":"All bookings cleared."})
