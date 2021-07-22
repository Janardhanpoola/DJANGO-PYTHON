from django.shortcuts import render

# Create your views here.

def store(request):
    content={}
    return render(request,'store.html')

def cart(request):
    content={}
    return render(request,'cart.html')

def checkout(request):
    content={}
    return render(request,'checkout.html')    

