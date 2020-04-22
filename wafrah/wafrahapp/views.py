from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(req):
    return HttpResponse('<h1>Index</h1>')

def categories(req):
    return HttpResponse('<h1>test</h1>')