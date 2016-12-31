from __future__ import unicode_literals

from django.db import models


class Notice(models.Model):
    content=models.TextField()
    created_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


class Branch(models.Model):
    name=models.CharField(max_length=100)


class Board(models.Model):
    name=models.CharField(max_length=100)


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
    CLASS_CHOICES=(
        ('1','I'),
        ('2','II'),
        ('3','III'),
        ('4','IV'),
        ('5','V'),
        ('6','VI'),
        ('7','VII'),
        ('8','VIII'),
        ('9','IX'),
        ('10','X'),
        ('11','XI'),
        ('12','XII'),
    )
    name=models.CharField(max_length=100)
    mothers_name=models.CharField(max_length=100)
    date_of_birth=models.DateField()
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES)
    address=models.TextField()
    contact_number=models.CharField(max_length=13)
    email_address=models.EmailField()
    school_name=models.CharField(max_length=100)
    school_board=models.ForeignKey(Board)
    school_class=models.CharField(max_length=5,choices=CLASS_CHOICES)
    subjects=models.ManyToManyField(Subject)
    preferred_branch=models.ForeignKey(Branch)
    joined_on=models.DateTimeField(auto_now=True)


class Faculty(models.Model):
    name=models.CharField(max_length=100)
    address=models.TextField()
    contact_number=models.CharField(max_length=13)
    email_address=models.EmailField()
    high_school=models.ForeignKey(Qualification,related_name='high_school')
    intermediate=models.ForeignKey(Qualification,related_name='intermediate')
    highest_qualification=models.ForeignKey(Qualification,related_name='highest_qualification')
    joined_on=models.DateTimeField(auto_now=True)


class Testimonial(models.Model):
    content=models.TextField()
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.content