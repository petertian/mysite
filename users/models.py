from django.db import models
# Create your models here.
class Employee(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	nickname = models.CharField(max_length=30)
	sex = models.CharField(max_length=10,blank=True)
	email = models.EmailField(max_length=75,blank=True)
	phone = models.IntegerField(max_length=20)
	mobile = models.IntegerField(max_length=40)
	password = models.CharField(max_length=30,blank=True)
	city = models.CharField(max_length=10,blank=True)
	department = models.CharField(max_length=30,blank=True)
	ip = models.IPAddressField()

	def  __unicode__(self):
		return self.name
class Package(models.Model):
	name = models.CharField(max_length=30)
	phone = models.IntegerField(max_length=10)
	date = models.DateField()

	def __unicode__(self):
		return unicode(self.phone)