from django.shortcuts import render

from .models import destination

# Create your views here.

def index(request):

    dests=destination.objects.all

    return render(request,'index.html',{'dests':dests})

def dest(request):
    dests=destination.objects.all
    return render(request,'destination.html',{'dests':dests})
