from tokenize import Name
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
# Create your views here.


def index(request):
    return render(request,"app/index3.html")

def about(request):
    return render(request,"app/about.html")





    
 







    
