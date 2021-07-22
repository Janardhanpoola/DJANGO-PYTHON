from django.http import HttpResponse

from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')

def count(request):
    if request.method=='POST':
        content=request.POST['fulltext']  #this will fetch the content that we typed in textarea 
        content=content.replace("\n"," ")
        content=content.replace("\r"," ")
        content=content.split(" ")
        content=[i for i in content if i!=""]
        wdict={}
        for word in content:
            if word in wdict:
                wdict[word]+=1
            else:
                wdict[word]=1
        
        sorted_lst=sorted(wdict.items(),key=lambda wdict:wdict[1],reverse=True) 
        most_occ=sorted_lst[0]
        #most_occ=dict(list(sorted_dict.items())[0:2])

        total=len(content)
        #print(total)
        return render(request,'count.html',{"fulltext":content,"countword":total,"wdict":wdict,"most_occ":most_occ})

def about(request):
    return render(request,'about.html')