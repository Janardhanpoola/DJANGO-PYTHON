from django.shortcuts import redirect

from django.http import HttpResponse

def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group=None
            if request.user.groups.exists:
                group=request.user.groups.all()[0].name #getting user group defined
                print(group)
            if group in allowed_roles:
                return view_func(request,*args,**kwargs)
            
            else:
                return HttpResponse("You're not authorized to view this page")
            return view_func(request,*args,**kwargs)
        return wrapper_func
    return decorator


def admin_only(view_func): #this is for (customer) redirecting to the user-page when he goes to home-page from "http://localhost:8000/user-page/" 
    def wrapper_func(request,*args,**kwargs):
        group=None
    
        if request.user.groups.exists:
            group=request.user.groups.all()[0].name

        if group=='customer':
            return redirect('user-page')

        if group=='admin':
            return view_func(request,*args,**kwargs)
    return wrapper_func
