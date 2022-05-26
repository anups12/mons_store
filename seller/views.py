from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *
from customer.models import *
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.


def Create_User(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in as '+ request.user.username)
        return redirect('/seller/profile/')
    else:
        form = UserCreate()
        if request.method=='POST':
            form = UserCreate(request.POST)
            print(request.POST)
            if form.is_valid():
                user = form.save()
                Seller.objects.create(user=user, name=user.username, email=user.email)
                messages.success(request, 'Seller has been created')
                return redirect('/logincust/')
        context={'form':form}
        return render(request, 'seller/createseller.html', context)

def LoginUser(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in ')
        return redirect('/seller/profile/')
    else:
        if request.method=='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in as '+ request.user.username)
                return redirect('/seller/profile/')
        return render(request, 'seller/login.html')
@login_required
def Profile(request):
    user = Seller.objects.get(user=request.user)
    product = Product.objects.filter(seller=request.user.seller)
    context = {'user':user, 'product':product}
    return render(request, 'seller/profile.html', context)

@login_required
def Update_Profile(request, pk):
    user = request.user.seller  
    form = UpdateSeller(instance=user)
    if request.method=='POST':
        form = UpdateSeller(request.POST, request.FILES, instance=user)
       
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile has been Updated ')
            return redirect('/seller/profile/')
    context={'form':form}
    return render(request, 'seller/updateseller.html', context)


def LogoutUser(request):
    logout(request)
    messages.warning(request, 'You have been logged out login to see your account')
    return redirect('/logincust/')

@login_required
def Product_Add(request):
    main = Maincategory.objects.all()
    sub = Subcategory.objects.all()
    seller= request.user.seller
    form = ProductAdd(instance=seller)
    if request.method=='POST':
        form = ProductAdd(request.POST, request.FILES, instance=seller)
        if form.is_valid():
            name = form.cleaned_data['name']
            mc = form.cleaned_data['maincategory']
            sc = form.cleaned_data['subcategory']
            brand = form.cleaned_data['brand']
            baseprice = form.cleaned_data['baseprice']
            discount = form.cleaned_data['discount']
            finalprice = form.cleaned_data['finalprice']
            desc = form.cleaned_data['description']
            size = form.cleaned_data['size']
            color = form.cleaned_data['color']
            stock = form.cleaned_data['stock']
            pic1 = form.cleaned_data['pic1']
            pic2 = form.cleaned_data['pic2']
            pic3 = form.cleaned_data['pic3']
            pic4 = form.cleaned_data['pic4']
            prod = Product(name=name,maincategory=mc,subcategory=sc,brand=brand,baseprice=baseprice,description=desc, discount=discount,finalprice=finalprice,size=size,color=color,stock=stock,pic1=pic1,pic2=pic2,pic3=pic3,pic4=pic4,seller=seller)
            prod.save()
            messages.success(request, 'Product has been added successfully')
            return redirect('/seller/profile/')    
    context={'form':form,'main':main, 'sub':sub}
    return render(request, 'seller/product.html', context)

@login_required
def UpdateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductAdd(instance=product)
    if request.method=='POST':
        form =ProductAdd(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product has been Updated successfully')
            return redirect('/seller/profile/')
    context = {'form':form}
    return render(request, 'seller/updateproduct.html', context)

def ProductDetail(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product':product}
    return render(request, 'customer/productdetail.html', context)