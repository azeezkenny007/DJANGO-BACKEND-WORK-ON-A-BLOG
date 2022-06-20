from django.shortcuts import render
from .decorators import *
from .models import *

# Create your views here.
def error(request):
    return render(request,'pages/404.html')
def about(request):
    return render(request,'pages/about.html')
def catalog1(request):
    return render(request,'pages/catalog1.html')
def catalog2(request):
    return render(request,'pages/catalog2.html')
def details1(request):
    return render(request,'pages/details1.html')
def details2(request):
    return render(request,'pages/details2.html')
def faq(request):
    return render(request,'pages/faq.html')
@ authenticate
def index(request):
    film=Film.objects.all()
    kate={'film':film}
    print(request.user)
    return render(request,'pages/index.html',context=kate)
def index2(request):
    return render(request,'pages/index2.html')
def pricing(request):
    return render(request,'pages/pricing.html')
