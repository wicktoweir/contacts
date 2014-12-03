from django.db import models
from django.contrib.auth.models import User

# PHONE TABLE ELEMENTS
class Phone(models.Model):
	NUMBER_TYPE_CHOICES = (
		('H', 'Home'),
		('C', 'Cell'),
		('W', 'Work'),
		('F', 'Fax'),
	)
	number_type = models.CharField(max_length=1, choices=NUMBER_TYPE_CHOICES, default='H')
	number = models.CharField(max_length=20)
	created = models.DateTimeField(auto_now_add=True) 
	last_modified = models.DateTimeField(auto_now=True)

class UserPhone(models.Model):
	user = models.ForeignKey(User)
	phone = models.ForeignKey(Phone)

#EMAIL TABLE ELEMENTS
class Email(models.Model):
	EMAIL_TYPE_CHOICES = (
		('P', 'Personal'),
		('W', 'Work'),
		('S', 'Shared'),
	)
	email_type = models.CharField(max_length=1, choices=EMAIL_TYPE_CHOICES, default='P')
	email = models.CharField(max_length=200)
	created = models.DateTimeField(auto_now_add=True) 
	last_modified = models.DateTimeField(auto_now=True)

class UserEmail(models.Model):
	user = models.ForeignKey(User)
	phone = models.ForeignKey(Email)




