# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from users.models import Employee
from django.shortcuts import render_to_response,RequestContext
from django.contrib import auth
from django.contrib.auth import authenticate,login
from django.views.decorators.csrf import csrf_protect
def login(request):
	if request.META.has_key('HTTP_X_FORWARDED_FOR'):
		host_ip = request.META['HTTP_X_FORWARDED_FOR']
	else:
		host_ip = request.META['REMOTE_ADDR']
	user_name = Employee.objects.get(ip=host_ip).nickname
	return render_to_response('index.html',{'user_name':user_name})
	context = {}
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user  =authenticate(username=username,password=password)
		if request.user.is_authenticated():
			return HttpResponseRedirect('/')

def register(request):
	return HttpResponse("register.page")
@csrf_protect
def user_view(request):
	cxt={}
	context.update(csrf(request))
	if request.user.is_authenticated():
		return render_to_response('user.html',cxt,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/")
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')