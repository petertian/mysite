from django.contrib import admin
from mysite.users.models import Employee, Package

admin.site.register(Employee)
admin.site.register(Package)