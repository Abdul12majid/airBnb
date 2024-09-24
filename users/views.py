from django.shortcuts import render, HttpResponse
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def login_user(request):
	return HttpResponse("Login view")