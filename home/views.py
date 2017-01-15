from django.shortcuts import render
from .models import Notice, Testimonial
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import Group


def index(request):
    data=dict()
    data['notices']=Notice.objects.all()
    data['testimonials']=Testimonial.objects.all()
    return render(request,'home/index.html',data)


def disclaimer(request):
    return render(request,'home/disclaimer.html')


def user_login(request):
    data=dict()
    if request.method=='POST':
        username=request.POST['userid']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            if user in Group.objects.get(name='students').user_set.all():
                return render(request,'home/student.html',data)
            elif user in Group.objects.get(name='faculties').user_set.all():
                return render(request,'home/faculty.html',data)
            elif user in Group.objects.get(name='admin').user_set.all():
                return render(request,'home/admin.html',data)
            else:
                data['result']=False
                data['msg']='Cannot recognize you'
        else:
            data['result']=False
            data['msg']='Username and Password combination is incorrect! Try again.'
    return render(request,'home/login.html',data)
