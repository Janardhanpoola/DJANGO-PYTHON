from django.shortcuts import render,redirect

from django.contrib import messages

# Create your views here.
from django.contrib.auth.models import User,auth #for creating user and save that user in database


def signup(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']

        # if not first_name or not last_name or not username or not password2 or not password1 or not email :
        #     messages.info(request,'please fill in all the fields')  #use required field in html 
        #     return redirect('/auth/signup')

        spcl_chars=['$','&','*','#','@']
        
        if len(password1)<6:
            messages.info(request,"PWD should be atleast 6 chars")
            return redirect('/auth/signup')
        if len(password1)>12:
            messages.info(request,"pwd too long")
            return redirect('/auth/signup')

        if not any(char.isdigit() for char in password1):
            messages.info(request,"atleast 1 digit")
            return redirect('/auth/signup')
        
        if not any(char.isupper() for char in password1):
            messages.info(request,"atleast one upper")
            return redirect('/auth/signup') 

        if not any(char.islower() for char in password1):
            messages.info(request,"atleast 1 lower")
            return redirect('/auth/signup')                       
        if not any(char in spcl_chars for char in password1):
            messages.info(request,"atleast one spcl char")
            return redirect('/auth/signup')   


        if password1==password2:
            if User.objects.filter(username=username).exists() :
                messages.info(request,'username taken')
                return redirect('/auth/signup')
            elif username.isdigit() or username.isalpha():
                messages.info(request,'username should contain alnum')
                return redirect('/auth/signup')                
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')   
                return redirect('/auth/signup')
                             
            else:
                user=User.objects.create_user(username=username,password=password1,first_name=first_name ,last_name=last_name,email=email) #1st argument is the exact name as in django auth_user columns,2nd arg is you passing above
                user.save()
                return redirect('/auth/login')
                
        else:
                messages.info(request,'pwds not matching')
                return redirect('/auth/signup')
    else:
        
        return render(request,'signup.html')
        #return redirect('/auth/signup')



def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None: #if the user is already registered
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid user')
            return redirect('/auth/login/')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')   