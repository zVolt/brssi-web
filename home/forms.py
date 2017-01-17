from django import forms
from django.db import models
from django.forms import ModelForm,TextInput,DateInput,Select,SelectMultiple,Textarea,NumberInput,EmailInput
from .models import Student

class LoginForm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=100)


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'mothers_name', 'date_of_birth','gender','address','contact_number','email_address','school_name','school_board','school_class','subjects','preferred_branch']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control','placeholder': 'Your full name'}),
            'mothers_name': TextInput(attrs={'class': 'form-control','placeholder': 'Mother\'s full name'}),
            'date_of_birth': DateInput(attrs={'class': 'form-control','placeholder': 'Your birth date'}),
            'gender': Select(attrs={'class': 'form-control','placeholder': 'Gender'}),
            'address': Textarea(attrs={'class': 'form-control','placeholder': 'where do you live?'}),
            'contact_number': NumberInput(attrs={'class': 'form-control','placeholder': 'your contact number'}),
            'email_address': EmailInput(attrs={'class': 'form-control','placeholder': 'your email address'}),
            'school_name':TextInput(attrs={'class':'form-control','placeholder':'school_name'}),
            'school_board':Select(attrs={'class':'form-control','placeholder':'school_board'}),
            'school_class':Select(attrs={'class':'form-control','placeholder':'school_class'}),
            'subjects':SelectMultiple(attrs={'class':'form-control','placeholder':'subjects'}),
            'preferred_branch':Select(attrs={'class':'form-control','placeholder':'preferred_branch'})

        }
