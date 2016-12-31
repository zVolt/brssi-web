from django.shortcuts import render
from . models import Notice, Testimonial


def index(request):
    data=dict()
    data['notices']=Notice.objects.all()
    data['testimonials']=Testimonial.objects.all()
    return render(request,'home/index.html',data)


def disclaimer(request):
    print 'disclaimer'
    return render(request,'home/disclaimer.html')