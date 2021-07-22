from django.shortcuts import render

#from django.urls import request

def home(request):
    return render(request,'home.html')

def add(request):
    n1=request.POST["num1"]
    n2=request.POST["num2"]

    res=int(n1)+int(n2)

    return render(request,'result.html',{'result':res})
