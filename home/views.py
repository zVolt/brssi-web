from django.shortcuts import render
from .models import Notice, Testimonial
from .forms import LoginForm

def index(request):
    data=dict()
    data['notices']=Notice.objects.all()
    data['testimonials']=Testimonial.objects.all()
    return render(request,'home/index.html',data)


def disclaimer(request):
    return render(request,'home/disclaimer.html')

def login(request):
    data=dict()
    if request.method=='GET':
        data['login_form']=LoginForm()
        return render(request,'home/login.html',data)
    elif request.method=='POST':
        data['login_form']=LoginForm()
        return render(request,'home/login.html',data)
