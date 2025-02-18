from django.shortcuts import render 
from django.http import HttpResponse 
#Create your views here. 
def home (request): 
     return render(request, 'app/home.html')
# good_exchange_app/views.py

def about(request):
    return render(request, 'app/about.html')

def login(request):
    return render(request, 'app/login.html')

def register(request):
    return render(request, 'app/register.html')

def contact(request):
    return render(request, 'app/contact.html')

def list1(request):
    return render(request, 'app/list1.html')

def list2(request):
    return render(request, 'app/list2.html')

def dstd(request):
    return render(request, 'app/dstd.html')

def list3(request):
    return render(request, 'app/list3.html')

def list4(request):
    return render(request, 'app/list4.html')

def see(request):
    return render(request, 'app/see.html')


