from django.shortcuts import render
from django.http import HttpResponse

items = [
    {
        'category':'food',
        'name':'coffee',
        'amount':'100kgs'
    },
    {
        'category':'food',
        'name':'sugar',
        'amount':'1000kgs'
    }
]

# Create your views here.
def home(req):
    context = {
        'items':items
    }
    return render(req, 'index.html',context)

def categories(req):
    return render(req, 'categories.html')

def productView(req):
    return render(req, 'productView.html')

def login(req):
    return render(req, 'login.html')

def signup(req):
    return render(req, 'signup.html')