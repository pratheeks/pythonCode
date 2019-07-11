from django import forms

class EmployeeRegister(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	age = forms.IntegerField()