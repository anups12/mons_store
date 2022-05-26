import json
from . models import *

def GetCookie(request):
    try:
        cart= json.loads(request.COOKIES['cart'])
    except:
        cart={}
    item=[] 
    order = {'Total_quantity':0, 'Total_price':0, 'shipping':False}
    cartitem =  order['Total_quantity']
    for i in cart:
        try:
            cartitem += cart[i]['quantity']
            product= Product.objects.get(id=i)
            order['Total_quantity']+=cart[i]['quantity']
            order['Total_price']+=product.finalprice*cart[i]['quantity']
            item1={
                'product':{
                    'id':product.id,
                    'price':product.finalprice,
                    'name':product.name,
                    'pic1':product.pic1.url
                },
                'quantity':cart[i]['quantity'],
                'get_total':product.finalprice*cart[i]['quantity']
            }
            item.append(item1)
        except:
            pass
    return {'item':item, 'order':order, 'cartitem':cartitem}


def cartData(request):
    try:
        if request.user.is_authenticated:   
            customer= request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, completed=False)
            item = order.orderitem_set.all
            cartitem = order.Total_quantity
        else:
            cookiedata=GetCookie(request)
            cartitem=cookiedata['cartitem']
            order=cookiedata['order']
            item=cookiedata['item']
        return {'item':item, 'order':order, 'cartitem':cartitem,'order':order}
    except:
        cartitem={''}
        return cartitem
   