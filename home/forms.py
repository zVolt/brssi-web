from django import forms
from django.db import models
from django.forms import ModelForm,TextInput,DateInput,Select,SelectMultiple,Textarea,NumberInput,EmailInput,CheckboxInput,BooleanField,RadioSelect
from .models import Student,Scholarship


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


class ScholarshipForm(ModelForm):
    declaration = BooleanField(label='I agree')
    class Meta:
        model = Scholarship
        fields = ['marks_in_board_exam','marks_in_institute_exam','monthly_family_income','other_scholarship','declaration']
        widgets = {
            'marks_in_board_exam': NumberInput(attrs={'class': 'form-control','placeholder': 'Marks in board examinations'}),
            'marks_in_institute_exam': NumberInput(attrs={'class': 'form-control','placeholder': 'Marks in BRSSI examinations'}),
            'monthly_family_income': NumberInput(attrs={'class': 'form-control','placeholder': 'Monthly income in rupees'}),
            'other_scholarship': RadioSelect(attrs={'class': 'radio',},choices=((True,'Yes'),(False,'No'))),
        }
        labels = {
            'other_scholarship': 'Do you receive any scholarship from other source ?',
            'marks_in_board_exam': 'Marks obtained in Board exam (in percentage)',
            'marks_in_institute_exam':'Marks obtained in Institute exam (in percentage)',
            'monthly_family_income':'Monthly family income in Rupees',
        }
