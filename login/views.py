from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
# Create your views here.

def home(request):
    return render(request,'index.html')

def login(request):
    u=request.POST["username"]
    p=request.POST["password"]
    
    return render(request,'a.html')