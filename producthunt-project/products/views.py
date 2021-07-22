from django.shortcuts import render,redirect,get_object_or_404   

from django.contrib.auth.decorators import login_required

from products.models import Product

from django.utils import timezone

def home(request):
    products=Product.objects
    return render(request,'products/home.html',{'products':products})


@login_required   #users can only create when they are logged in

def create(request):
    if request.method=='POST':
        if request.POST['Title'] and request.POST['Url'] and request.POST['body'] and request.FILES['image'] and request.FILES['icon']:
            product=Product()
            product.title=request.POST['Title']
            if request.POST['Url'].startswith('http://') or request.POST['Url'].startswith('https://'):
                product.url=request.POST['Url']
            else:
                product.url='http://'+request.POST['Url']
            product.body=request.POST['body']
            product.pic=request.FILES['image']
            product.icon=request.FILES['icon']
            product.pub_date=timezone.datetime.now()
            product.hunter=request.user
            product.save()
            return redirect('/products/'+str(product.id))
        else:
            return render(request,'products/create.html',{'error':'Fill all the fields'})
    
    else:

        return render(request,'products/create.html')


def detail(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    return render(request,'products/detail.html',{'product':product})

@login_required
def upvote(request,product_id):
        product=get_object_or_404(Product,pk=product_id)
        product.votes_total+=1
        product.save()
        return redirect('/products/'+str(product.id))
