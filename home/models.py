from __future__ import unicode_literals

from django.db import models


class Subject(models.Model):
	name=models.CharField(max_length=100)
	description=models.TextField()

class Qualification(models.Model):
	qualification_name=models.CharField(max_length=100)
	school=models.CharField(max_length=100)
	board=models.CharField(max_length=100)
	result=models.CharField(max_length=100)
	
class Student(models.Model):
	GENDER_CHOICES=(
		('Male','male'),
		('Female','female'),
		('Other','other')
	)
	name=models.CharField(max_length=100)
	mothers_name=models.CharField(max_length=100)
	date_of_birth=models.DateField(auto_now=True)
	gender=models.CharField(max_length=10,choices=GENDER_CHOICES)
	address=models.TextField()
	joined_on=models.DateTimeField(auto_now=True)

class Faculty(models.Model):
	name=models.CharField(max_length=100)
	address=models.TextField()
	contact_number=models.CharField(max_length=13)
	email_address=models.EmailField()
	high_school=models.ForeignKey(Qualification,related_name='high_school')
	intermediate=models.ForeignKey(Qualification,related_name='intermediate')
	highest_qualification=models.ForeignKey(Qualification,related_name='highest_qualification')


