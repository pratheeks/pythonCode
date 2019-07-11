from django.urls import path
from BankApp import views

urlpatterns = [
	path('update/',views.update_user), 
	path('delete/',views.delete_user),
	path('insert/',views.insert_user),


]