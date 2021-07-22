from django.shortcuts import render

from .models import Job  #for importing job objects


def home(request):
    jobs=Job.objects #this stores all the job items stored in DB
    return render(request,'jobs/home.html',{"jobs":jobs})    
