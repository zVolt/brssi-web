from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Notice(models.Model):
    content=models.TextField()
    created_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


class Branch(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Board(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.name


class Qualification(models.Model):
    qualification_name=models.CharField(max_length=100)
    school=models.CharField(max_length=100)
    board=models.CharField(max_length=100)
    result=models.CharField(max_length=100)



class Student(models.Model):
    GENDER_CHOICES=(
        ('male','Male'),
        ('female','Female'),
        ('other','Other')
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
    user=models.OneToOneField(User, on_delete=models.CASCADE)
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

    def __str__(self):
        return str(self.name)+'('+str(self.user.username)+')'


class Faculty(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    address=models.TextField()
    contact_number=models.CharField(max_length=13)
    email_address=models.EmailField()
    high_school=models.ForeignKey(Qualification,related_name='high_school')
    intermediate=models.ForeignKey(Qualification,related_name='intermediate')
    highest_qualification=models.ForeignKey(Qualification,related_name='highest_qualification')
    joined_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)+'('+str(self.user.username)+')'


class Testimonial(models.Model):
    content=models.TextField()
    name=models.CharField(max_length=100)
    # image=models.ImageField()
    def __str__(self):
        return str(self.content)+'('+str(self.name)+')'


class Test(models.Model):
    test_code=models.CharField(max_length=100)
    subject=models.ForeignKey(Subject)
    total_marks=models.CharField(max_length=50)


class TestAttempt(models.Model):
    student=models.ForeignKey(Student)
    test=models.ForeignKey(Test)
    faculty=models.ForeignKey(Faculty)
    date_of_examination=models.DateField(auto_now=True)
    marks_obtained=models.CharField(max_length=50)
    remarks=models.CharField(max_length=100)
