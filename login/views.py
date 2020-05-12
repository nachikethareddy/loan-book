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
    
    url = 'http://loan-book.herokuapp.com/auth/token/login/'

    myobj = {'username': u,'password':p}
    x = requests.post(url, data = myobj)
    data=json.loads(x.text)
    if 'auth_token' in data.keys():
        return render(request,'a.html',{'token':data['auth_token']})
    else:
        return render(request,'index.html',{'auth':'Inavalid username/password'})