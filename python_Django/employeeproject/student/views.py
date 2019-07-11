from django.shortcuts import render
from student.models import student
# Create your views here.

def display_stud(request):
	student_records=student.objects.all()
	my_dict={'records':student_records}
	return render(request,'record/record.html',my_dict)

