from django.shortcuts import render
from databaseApp import forms
# Create your views here.
def student_view(request):
	form_page=forms.studentForm
	my_dic={'form_page':form_page}

	if request.method=='POST':
		form_data=forms.studentForm(request.POST)
		if form_data.is_valid():
			form_data.save(commit=True)
			form_page=forms.studentForm

	return render(request,'databaseApp/input.html',context=my_dic)