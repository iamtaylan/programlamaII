from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def restoranlar(request):
    return render(request,'restoranlar.html')

def menuler(request, slug):
    return render(request,'menuler.html', {
        slug:slug
    })
