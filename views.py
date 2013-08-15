from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response,RequestContext
from users.models import Employee
import datetime
import getpass
from django.db import connection
from django.contrib import auth
def index(request):
	context = {}
	u_name = getpass.getuser()
	
	# num = len(emps)
	if request.user.is_authenticated():
		return HttpResponseRedirect("/user/")
	else:
		if Employee.objects.get(ip=host_ip).password:
			return HttpResponseRedirect("/user/login/")
		else:
			return render_to_response('register.html', {'user_name': user_name})

def about_pages(request, page):
	try:
		return direct_to_template(request, template="about/%s.html" % page)
	except TemplateDoesNotExist:
		raise Http404()
