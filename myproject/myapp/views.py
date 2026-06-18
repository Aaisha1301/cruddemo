from django.shortcuts import render,redirect,get_object_or_404
from .models import Product
from .forms import ProductForm
from django.core.paginator import Paginator
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
def product_list(request):
    search=request.GET.get('search')
    if search:
        product_list=Product.objects.filter(name__icontains=search)
    else:
        product_list=Product.objects.all()
    paginator=Paginator(product_list,5)
    page_number = request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request,'product_list.html',{'page_obj':page_obj,'search':search})
def add_product(request):
    form=ProductForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request,'product_form.html',{'form': form})


def update_product(request,id):
    product = get_object_or_404(Product,id=id)
    form=ProductForm(request.POST or None,request.FILES or None,instance=product)

    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request,'product_form.html',{'form': form})

def delete_product(request,id):
    product=get_object_or_404(Product,id=id)
    product.delete()
    return redirect('product_list')


    
def sign_in(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exists")
            return redirect('signin')
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        messages.success(request,"Account created successfully")
        return redirect('login')
        
    return render(request,'sign_in.html')

def user_login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request,user)
            return redirect('product_list')
        else:
            messages.error(request,"Invalid Username or Password")

    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')