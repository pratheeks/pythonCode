from django.shortcuts import render
import datetime
# Create your views here.
def greet_disp(request):
	time=datetime.datetime.now()
	h=int(time.strftime('%H'))

	if h<12:
		Msg="Good Morning World."
	elif h<16:
		Msg="Good Noon World."
	elif h<20:
		Msg="Good Evening World."
	elif h<24:
		Msg="Good Night World."

	my_dict={'ins_time':time,'ins_msg':Msg}

	return render(request,'GreetingImg/index.html',my_dict)
	