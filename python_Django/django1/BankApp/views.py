from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def update_user(request):
	s="<h1>Updating the Account</h1>"
	return HttpResponse(s)

def delete_user(request):
	s="<h1>Delete the Account</h1>"
	return HttpResponse(s)

def insert_user(request):
	s="<h1>Insert the Accountno.</h1>"
	return HttpResponse(s)
