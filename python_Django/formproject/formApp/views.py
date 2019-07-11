from django.shortcuts import render
from formApp import forms
# Create your views here.

def registration_view(request):
	form_page=forms.EmployeeRegister()
	if request.method=='POST':
		form_data=forms.EmployeeRegister(request.POST)
		if form_data.is_valid():
			print("Employee Data:")
			print("Employee Name:",form_data.cleaned_data['name'])
			print("Employee Email:",form_data.cleaned_data['email'])
			print("Employee Age:",form_data.cleaned_data['age'])
	my_dict={'insert_form':form_page}
	return render(request,'Registration/input.html',my_dict)