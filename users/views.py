# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from users.models import Employee
from django.shortcuts import render_to_response
from django.contrib import auth

def login(request):
	if request.method == "POST":
		try:
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = auth.authenticate(username=username,password=password)
			if user is not None and user.is_active:
				auth.login(request,user)
				return HttpResponseRedirect("/user/"+username)
			else:
				return HttpResponse('error')
		except Exception,e:
			return HttpResponse('error')
		return HttpResponse("POST")
def register(request):
	return HttpResponse("register.page")