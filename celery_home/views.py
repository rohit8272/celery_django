from django.shortcuts import render
from celery_django.celery import add
from celery_home.tasks import sub

# Create your views here.

def home(request):
    result = add.delay(10,16)
    print("result of add function: ",result)
    return render(request , 'index.html')

def about(request):
    result = sub.delay(20,11)
    print("result of sub function: ", result)
    return render(request , 'about.html')

def contact(request):
    return render(request , 'contact.html')