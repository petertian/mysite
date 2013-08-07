from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from users.models import Employee
import datetime
import getpass
from django.db import connection
from django.contrib import auth
def index(request):
	context = {}
	u_name = getpass.getuser()
	
	# num = len(emps)
	if request.META.has_key('HTTP_X_FORWARDED_FOR'):
		host_ip = request.META['HTTP_X_FORWARDED_FOR']
	else:
		host_ip = request.META['REMOTE_ADDR']
	user_name = Employee.objects.get(ip=host_ip).nickname
	if request.user.is_authenticated():
		return HttpResponseRedirect("/user/")
	else:
		if Employee.objects.get(ip=host_ip).password:
			return render_to_response('index.html', {'user_name': user_name})
		else:
			return render_to_response('register.html', {'user_name': user_name})
# def login(request):
# 	return render_to_response('login.html',)
# def login(request):
# 	errors = []
# 	if 's' in request.GET:
# 		values = request.GET['s']
# 		if not values:
# 			errors.append('Enter a search term.')
# 		elif len(values) > 20:
# 			errors.append('Please enter at most 10 characters.')
# 		else:
# 			books = Book.objects.filter(title__icontains=values)
# 			return render_to_response('search_results.html', {'books': books, 'query': values})
# 	return render_to_response('login.html', {'errors': errors})
def about_pages(request, page):
	try:
		return direct_to_template(request, template="about/%s.html" % page)
	except TemplateDoesNotExist:
		raise Http404()
