from datetime import datetime
import json
from django.db.models import Q
from .utils import *
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from customer.models import *
from seller.models import *
from django.contrib.auth import logout, login, authenticate
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


# Create your views here.
def Home(request):
    product = Product.objects.all()
    product = product[::-1]
    men= Product.objects.filter(maincategory=Maincategory.objects.get(name='Men'))
    women= Product.objects.filter(maincategory=Maincategory.objects.get(name='Women'))
    kid= Product.objects.filter(maincategory=Maincategory.objects.get(name='Kids'))
    electronics= Product.objects.filter(maincategory=Maincategory.objects.get(name='Electronics'))
    try:
        if  request.user.seller:
            cartitem={''}
    except:
        cartdata=cartData(request)
        cartitem=cartdata['cartitem']

    context={'men':men, 'women':women, 'kids':kid, 'product':product,'cartitem':cartitem, 'electronics':electronics}
    return render(request, 'customer/home.html', context)


def Create_Customer(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in as '+ request.user.username)
        return redirect('/')
    else:
        form = UserCreate()
        if request.method=='POST':
            form = UserCreate(request.POST)
            if form.is_valid():
                user = form.save()
                Customer.objects.create(user=user, name=user.username, email=user.email)
                messages.success(request, 'User created Successfully '+ user.username)
                return redirect('/logincust/')
        context={'form':form}
        return render(request, 'customer/createcustomer.html', context)

def CustomerLogin(request): 
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user) 
                messages.success(request, 'You are  logged in as '+ request.user.username)
                try:
                    if request.user.customer:
                        return redirect('/')
                except:
                    return redirect('login')
            else:
                messages.warning(request, "Either your username or password is wrong")
    return render(request, 'customer/login.html')

@login_required
def ProfileCustomer(request):
    cartdata=cartData(request)
    cartitem=cartdata['cartitem']   
    item=cartdata['item']
    cartitem=cartdata['cartitem'] 
    user = Customer.objects.get(user=request.user)
    orders=Order.objects.filter(completed='True', customer=request.user.customer)
    orders=orders[::-1]
    context = {'user':user,'item':item, 'cartitem':cartitem,'orders':orders }
    return render(request, 'customer/profile.html', context)

@login_required
def Update_Profile_customer(request):
    user = request.user.customer  
    form = UpdateCustomer(instance=user)
    if request.method=='POST':
        form = UpdateCustomer(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Profile has been updated successfully ')
            return redirect('/profilecust/')
    context={'form':form}
    return render(request, 'customer/updatecustomer.html', context)

@login_required
def CustomerLogout(request):
    logout(request)
    messages.warning(request, 'Your have logged out  ')
    return redirect('/logincust/')

def Shop(request, mc, sc, br):
    maincategory = Maincategory.objects.all()
    subcategory = Subcategory.objects.all()
    subc = Subcategory.objects.filter(maincategory = Maincategory.objects.get(id=1))
    brand= Brand.objects.all()
    if mc=='All' and sc=='All' and br=='All':
        product = Product.objects.all() 
    elif mc!='All' and sc=='All' and br=='All':
        product =Product.objects.filter(maincategory=Maincategory.objects.get(name=mc))
    elif mc=='All' and sc!='All' and br=='All':
        product =Product.objects.filter(subcategory=Subcategory.objects.get(name=sc))
    elif mc=='All' and sc=='All' and br!='All':
        product =Product.objects.filter(brand=Brand.objects.get(name=br))
    elif mc!='All' and sc!='All' and br=='All':
        product =Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc))
    elif mc!='All' and sc=='All' and br!='All':
        product =Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),brand=Brand.objects.get(name=br))
    elif mc=='All' and sc!='All' and br!='All':
        product =Product.objects.filter(brand=Brand.objects.get(name=br),subcategory=Subcategory.objects.get(name=sc))
    elif mc!='All' and sc!='All' and br!='All':
        product =Product.objects.filter(brand=Brand.objects.get(name=br),subcategory=Subcategory.objects.get(name=sc),maincategory=Maincategory.objects.get(name=mc))
    try:
        if request.user.seller:
            cartitem={''}  
            item={}
            order={}
    except:
            cartdata=cartData(request)
            cartitem=cartdata['cartitem']  
            order=cartdata['order']
            item=cartdata['item']
       
    if request.method=='POST':
        search=request.POST.get('search')
        product=Product.objects.filter(Q(name__icontains=search))
    context = {'product':product,'mc':mc,'maincategory':maincategory,'subcategory':subcategory ,'sc':sc, 'brand':brand, 'subc':subc,'br':br,'item':item, 'order':order, 'cartitem':cartitem}
    return render(request, 'customer/shop.html', context)

def ProductDetail(request, pk):
    try:
        if request.user.seller:
            cartitem={}
            item={}
    except:
            cartdata=cartData(request)
            cartitem=cartdata['cartitem']  
            item=cartdata['item']
       
    product = Product.objects.get(id=pk)
    context = {'product':product, 'item':item, 'cartitem':cartitem}
    return render(request, 'customer/productdetail.html', context)



def Wishlistprod(request, pk=None):
    if request.user.is_authenticated:
        if pk is not None:
            customer = Customer.objects.get(user=request.user)
            product = Product.objects.get(id=pk)
            wish = Wishlist(customer=customer,product=product)
            wishlist = Wishlist.objects.filter(customer=customer,product=product).exists()
            if wishlist:
                messages.info(request, 'This product is already in your wishlist ')
            else:
                wish = Wishlist(customer=customer,product=product)
                wish.save()
                messages.success(request, 'This product is added in your wishlist ')
            return redirect('/wishlist/')
        else:
            list = Wishlist.objects.filter(customer= request.user.customer)
            wishlistitems= list.count()
            cartdata=cartData(request)
            cartitem=cartdata['cartitem']  
            sum=0
            for pro in list:
                sum+=pro.product.finalprice
            final_price=sum 
    else:
        messages.success(request, 'You need to login to first ')
        return redirect('/logincust/')
    context = {'wishlistitems':wishlistitems,'list':list,'final_price':final_price,'cartitem':cartitem}
    return render(request, 'customer/wishlist.html', context)


@login_required(login_url='/logincust/')
def DeleteWishlist(request, pk):
    wish = Wishlist.objects.get(id=pk)
    wish.delete()
    messages.success(request, 'The product is deleted from your wishlist ')
    return redirect('/wishlist/')

def Cart(request):
    cartdata=cartData(request)
    cartitem=cartdata['cartitem']  
    item=cartdata['item']
    order=cartdata['order']
    context={'item':item, 'order':order, 'cartitem':cartitem}
    return render(request, 'customer/cart.html', context)

def Update_cart(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, completed=False)
    orderitem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action =='add':
        orderitem.quantity +=1
        messages.success(request, 'Product has been added to cart  ')
    elif action == 'remove':
        orderitem.quantity -=1
    orderitem.save()
    if orderitem.quantity<=0:
        orderitem.delete()
        messages.warning(request, 'Product has been removed ')

    return JsonResponse('Data added successfully', safe=False)

@login_required(login_url='/logincust/')
def Checkout(request):
    cartdata=cartData(request)
    cartitem=cartdata['cartitem']  
    item=cartdata['item']
    order=cartdata['order']
    if request.method== 'POST':
        customer=request.user.customer
        name= request.POST.get('name')
        phone= request.POST.get('phone')
        address= request.POST.get('address')
        city= request.POST.get('city')
        state= request.POST.get('state')
        pincode= request.POST.get('pincode')
        ship = Shipping(customer=customer,order=order,name=name,phone=phone,address=address,city=city,state=state,pincode=pincode)
        ship.save()
        return redirect('/payment/')
   
    context={'item':item, 'order':order, 'cartitem':cartitem}
    return render(request, 'customer/checkout.html', context)

def PaymentPage(request):
    cartdata=cartData(request)
    cartitem=cartdata['cartitem']  
    order=cartdata['order']
    if request.method=='POST':
        customer= request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        order.completed=True
        order.trans_id = datetime.now().timestamp()
        order.save()
        return redirect('/')
    context={ 'order':order,'cartitem':cartitem }
    return render(request, 'customer/payment.html',context)

def ChangePassword(request):
    return render(request,'customer/payment.html' )

def ContactUs(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')

        formdata = ContactForm(name=name, email=email, subject=subject, phone=phone, description=desc)
        formdata.save()
        send_mail(
        'Confirmation: Request submitted  ',
        '''
        Deer : Sir 
        from : Mons-tore.com,

        We have received your query and will contact you soon 
        Thanks and regards from Mon-store
        ''',
        'bossaman102@gmail.com',
        [email],
        fail_silently=False,
    )
    return render(request, 'customer/contact.html')