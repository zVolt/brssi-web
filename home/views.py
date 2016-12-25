from django.shortcuts import render

# Create your views here.
def index(request):
	print 'index'
	return render(request,'home/index.html')

def disclaimer(request):
	print 'disclaimer'
	return render(request,'home/disclaimer.html')