from django import forms
from django.db import models
from django.forms import ModelForm,TextInput,DateInput,Select,SelectMultiple,Textarea,NumberInput,EmailInput,CheckboxInput,BooleanField,RadioSelect
from .models import Student,Scholarship
from django.contrib.auth.models import User
from nocaptcha_recaptcha.fields import NoReCaptchaField

class UserForm(forms.Form):
    full_name = forms.CharField(min_length=3, widget=TextInput(attrs={'class': 'form-control','placeholder': 'Full name'}))
    email = forms.EmailField(widget=TextInput(attrs={'class': 'form-control','placeholder': 'Email'}))

class LoginForm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=100)


class StudentForm(ModelForm):
    full_name = forms.CharField(min_length=3, widget=TextInput(attrs={'class': 'form-control','placeholder': 'Full name'}))
    email = forms.EmailField(widget=TextInput(attrs={'class': 'form-control','placeholder': 'Email'}))
    username = forms.CharField(min_length=3, widget=TextInput(attrs={'class': 'form-control','placeholder': 'Username'}))
    captcha = NoReCaptchaField()
    class Meta:
        model = Student
        fields = ['full_name','email','username','mothers_name', 'date_of_birth','gender','contact_number','school_name','school_board','school_class','subjects','preferred_branch','address','captcha']
        widgets = {
            #'user__lastname': TextInput(attrs={'class': 'form-control','placeholder': 'Your full name'}),
            'mothers_name': TextInput(attrs={'class': 'form-control','placeholder': 'Mother\'s full name'}),
            'date_of_birth': DateInput(attrs={'class': 'form-control','placeholder': 'Your birth date'}),
            'gender': Select(attrs={'class': 'form-control','placeholder': 'Gender'}),
            'address': Textarea(attrs={'class': 'form-control','placeholder': 'where do you live?'}),
            'contact_number': NumberInput(attrs={'class': 'form-control','placeholder': 'your contact number'}),
            #'email_address': EmailInput(attrs={'class': 'form-control','placeholder': 'your email address'}),
            'school_name':TextInput(attrs={'class':'form-control','placeholder':'school_name'}),
            'school_board':Select(attrs={'class':'form-control','placeholder':'school_board'}),
            'school_class':Select(attrs={'class':'form-control','placeholder':'school_class'}),
            'subjects':SelectMultiple(attrs={'class':'form-control','placeholder':'subjects'}),
            'preferred_branch':Select(attrs={'class':'form-control','placeholder':'preferred_branch'})
        }
    def save(self,commit=True):
        user=User(username=self.cleaned_data['username'],email=self.cleaned_data['email'])
        name=self.cleaned_data['full_name'].split()
        if len(name)==1:
            user.first_name=name[0]
        elif len(name)==2:
            user.first_name=name[0]
            user.last_name=name[1]
        else:
            user.first_name=' '.join(name[:-1])
            user.last_name=name[-1]
        if commit:
            user.save()
            student=super(StudentForm,self).save(commit=False)
            student.user=user
        return super(StudentForm,self).save(commit=commit)

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
