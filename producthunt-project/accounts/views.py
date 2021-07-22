from django.shortcuts import render,redirect

from django.contrib.auth.models import User #for user object

from django.contrib import auth #auth details


def signup(request):

    if request.method=="POST":
        if request.POST["password1"]==request.POST["password2"]:# ensuring both the pwds are correct
            try:
                user=User.objects.get(username=request.POST["username"]) #if pwds are correct ,it checks if username is already taken
                return render(request,'accounts/signup.html',{'error':'username is already taken'})
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['username'],request.POST['password1']) #if user is new,it redirects to home page
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'accounts/signup.html',{'error':'please enter correct pwds in both tabs'})

    else:
        return render(request,"accounts/signup.html")

def login(request):

    if request.method=='POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password']) #it will try to authenticate the user..returns None if not authenticated.

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/login.html',{'error':'Username or password is incorrect'})


    else:
        return render(request,"accounts/login.html")    


def logout(request):
    if request.method=='POST':
        auth.logout(request)        
        return redirect('home')