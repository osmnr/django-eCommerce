from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request,'shop/home.html')

def shop(request):
     return render(request,'shop/shop.html')

def shopgrid(request):
    return render(request,'shop/shopgrid.html')

def shopdetail(request):
     return render(request,'shop/shopdetail.html')