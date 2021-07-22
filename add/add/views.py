from django.shortcuts import render
def add(request):
    d={'a':9,'b':10}
    sum=d['a']+d['b']
    return render(request,'add.html',{'sum':sum})