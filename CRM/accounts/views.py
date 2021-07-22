from django.shortcuts import render,redirect

#from django.http import HttpResponse
from django.forms import inlineformset_factory

from django.contrib.auth.forms import UserCreationForm # this is django registration form

from django.contrib.auth import authenticate,login,logout

from django.contrib import messages #inorder to display success message

from django.contrib.auth.decorators import login_required

from accounts.models import *

from .forms import OrderForm

# Create your views here.

from .filters import OrderFilter

from .forms import CreateUserForm,CustomerSettingsForm

from .decorators import unauthenticated_user,allowed_users,admin_only

from django.contrib.auth.models import Group

@unauthenticated_user
def loginpage(request):

    # if request.user.is_authenticated: #if user is authenticated we dont want them to access register page ..so we redirect them to home page
    #     return redirect('home')
    # else:

    if request.method=='POST':
        data=request.POST 
        username=data.get('username')
        pwd=data.get('password')
        user=authenticate(request,username=username,password=pwd)
        if user is not None: #that means he is already registered
            login(request,user)
            return redirect('home')
        
        else:
            messages.info(request,"Username or pwd is incorrect")

    context={}
    return render(request,'accounts/login.html',context)

@unauthenticated_user
def registerpage(request):
    # if request.user.is_authenticated: #if user is authenticated we dont want them to access register page ..so we redirect them to home page
    #     return redirect('home')
    # else:

    form=CreateUserForm() #this is django's default registration form

    if request.method=='POST':
        data=request.POST
        form=CreateUserForm(data)

        if form.is_valid():
            user=form.save()
            # group=Group.objects.get(name='customer') #we want registered users to be a part of customer group..so getting the group named customer

            # user.groups.add(group) #adding the user to customer group

            # Customer.objects.create( #assigning  customer a user profile(user) as and when registered
            #     user=user,
            #     name=user.username
            # )

            usern=request.POST.get('username')
           
            messages.success(request,'Account was created successfully for '+usern)
            return redirect('login')

    context={'form':form}
    return render(request,'accounts/register.html',context)

def logoutuser(request):

    logout(request)
    return redirect('login')


@login_required(login_url='login') #login url helps the unauthenticated users to go to login page
#@allowed_users(allowed_roles='admin') #only admin have rights to access dashboard
@admin_only
@allowed_users(allowed_roles='admin')
def home(request):

    #return HttpResponse("<h1>welcome to home</h1>")
    customers=Customer.objects.all()
    orders=Order.objects.all()
    last_5_orders=Order.objects.all().order_by('-id')[:5]

    total_orders=orders.count()
    orders_delivered=orders.filter(status='Delivered').count()
    orders_pending=orders.filter(status='Pending').count()
    context={'customers':customers,'orders':orders,'total_orders':total_orders,'orders_delivered':orders_delivered,'orders_pending':orders_pending,'last_5_orders':last_5_orders}

    return render(request,'accounts/home.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles='admin')

def products(request):
    #return HttpResponse("<h1>welcome to products</h1>")

    prods=Product.objects.all()

    context={'prods':prods}

    return render(request,'accounts/products.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles='admin')
def customer(request,pk):

    customer=Customer.objects.get(id=pk)  #setting the pk

    cust_orders=customer.order_set.all()

    cust_orders_total=customer.order_set.all().count()

    myFilter=OrderFilter(request.GET,queryset=cust_orders) #its gonna filter the data based on the GET data from the front end form

    cust_orders=myFilter.qs #reassigning(getting) the orders based on the filtered data

    context={'customer':customer,'cust_orders':cust_orders,'cust_orders_total':cust_orders_total,'myFilter':myFilter}

    return render(request,'accounts/customer.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles='admin')
def create_order(request,pk):
    customer=Customer.objects.get(id=pk)
    OrderFormSet=inlineformset_factory(Customer,Order,fields=['product','status'],extra=10) #1st arg: parent model,2nd arg child model and fields to be displayed in each form,extra -->how many fields to be displayed
    # inline formset are used to display multiple forms in a sinlgle form
    #form=OrderForm(initial={'customer':customer})  #initial automatically fills in  the field customer
    formset=OrderFormSet(instance=customer,queryset=Order.objects.none()) #queryset is for the existing fields to avoid filling in those fields if data already exists
    if request.method=='POST':
        data=request.POST  
        
        #form=orderForm(data)

        formset=OrderFormSet(data,instance=customer) # #taking the data submitted via frontend form and storing in modelform

        if formset.is_valid():
            formset.save()
        return redirect('/')

        
    context={'formset':formset,'customer':customer}
    return render(request,"accounts/orderform.html",context)

@login_required(login_url='login')
@allowed_users(allowed_roles='admin')
def update_order(request,pk):

    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)

    if request.method=='POST':
        data=request.POST
        form=OrderForm(data,instance=order)

        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}

    return render(request,'accounts/orderform.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles='admin')
def delete_order(request,pk):
    order=Order.objects.get(id=pk)

    form=OrderForm(instance=order)

    if request.method=="POST":
        order.delete()

        return redirect('/')

        
    context={'product':order}
    return render(request,'accounts/deleteorder.html',context)

@login_required
@allowed_users(allowed_roles='customer')

def userpage(request):
    
    cust_orders=request.user.customer.order_set.all()
    total_orders=request.user.customer.order_set.all().count()
    orders_pending=cust_orders.filter(status='Pending').count()
    orders_delivered=cust_orders.filter(status='Delivered').count()

    context={'cust_orders':cust_orders,'total_orders':total_orders,'orders_pending':orders_pending,'orders_delivered':orders_delivered}
    return render(request,'accounts/user.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles='customer')

def usersettings(request):
    customer=request.user.customer
    
    form=CustomerSettingsForm(instance=customer)

    if request.method=='POST':
        #data=request.POST
        form=CustomerSettingsForm(request.POST,request.FILES,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('user-settings')


    context={'form':form}
    return render(request,'accounts/usersettings.html',context)