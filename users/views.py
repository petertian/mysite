# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from users.models import Employee
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth import authenticate,login

def login(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return HttpResponse("ok")
		else:
			return HttpResponse('wrong')
def register(request):
	return HttpResponse("register.page")

def user_view(request):
	return render_to_response('user.html')