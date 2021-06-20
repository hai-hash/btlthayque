from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .decorators import allowed_user
from django.contrib.auth import authenticate, login
from collections import OrderedDict

def index(request):
    if request.user.is_authenticated:
        account = request.user
        customer = Customer.objects.get(account=account)
        chats = Chat.objects.filter(customer=customer)
    else:
        chats = []
    products = Product.objects.all()[:9]
    return render(request,"index.html",{"products":products,'chats':chats})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request,"login.html")

def product_detail(request,product_id):
    if request.user.is_authenticated:
        account = request.user
        customer = Customer.objects.get(account=account)
        rate = Rating.objects.filter(product__id=product_id,customer=customer)
    else:
        rate = []
    loves = Loves.objects.filter(product__id=product_id)
    if(len(loves) == 0):
        product1 = Product.objects.get(id=product_id)
        Loves.objects.create(product=product1)
    comments = Comment.objects.filter(product__id=product_id)
    love = Loves.objects.get(product__id=product_id)
    product = Product.objects.get(id=product_id)
    images = Image.objects.filter(product__id=product_id)
    product_discounts = Product_Discount.objects.filter(product__id=product_id,status = 1)
    discounts = []
    for discount in product_discounts:
        discounts.append(discount.discount)

    return render(request,"product_details.html",{'product':product,'images':images,'discounts':discounts,'comments':comments,'amount':len(rate),'love':love})

def clothes(request):
    clothes = Clothes.objects.all()
    return render(request,"products.html",{'books':clothes})

def book(request):
    book = Book.objects.all()
    return render(request,"products.html",{'books':book})
def electronic(request):
    electronics = Electronic.objects.all()
    return render(request,"products.html",{'books':electronics})

def search(request):
    name = request.GET['name']
    types = request.GET['type']
    if name == "":
        if types == "All":
            return redirect('home')
        elif types =="Book":
            return redirect('book')
        elif types == "Clothes":
            return redirect('clothes')
        else:
            return redirect('electronic')
    
    else:
        if types == "All":
            products = Product.objects.filter(name_product__icontains=name)
        else:
            products = Product.objects.filter(name_product__icontains=name,type=types)
    return render(request,"products.html",{'books':products})
    




@login_required(login_url="/login")
@allowed_user(allowed_role=["user"])

def cart(request):
    account = request.user
    items12 = ItemInCart.objects.filter(account=account,status=1)
    orders= InforOrder.objects.filter(customer__account=account)
    total = 0
    list_order = []
    for order in orders:
        order1 = Order()
        order1.order = order
        items = ItemInCart.objects.filter(order=order)
        order1.list_item = items
        list_order.append(order1)
    for item in items:
        total += item.total_price
    ships = Shipment.objects.all()
    address = ReceiveAddress.objects.filter(customer__account=account)
    payments = Payment.objects.all()
   
    return render(request,"product_summary.html",{'items':items12,'total':total,'amount':len(items12),'ships':ships,'orders':orders,'address':address,'payments':payments,'list_order':list_order})

def order(request,product_id):
    account = request.user
    product = Product.objects.get(id=product_id)
    color = request.GET['color']
    amount = request.GET['amount']
    discount_id = request.GET['discount_id']
    discount = Discount.objects.get(id = discount_id)
    total = product.price * int(amount)
    value_discount = discount.value + total*discount.phantram/100
    total_price = total - value_discount
    info = InforOrder.objects.get(id=1)
    ItemInCart.objects.create(product=product,account=account,amount=amount,color=color,discount=value_discount,total=total,total_price=total_price,order=info)
    return redirect('cart')

def deleteincart(request,item_id):
    ItemInCart.objects.get(id=item_id).delete()
    return redirect('cart')

def paymentconfirm(request):
    account = request.user
    customer = Customer.objects.get(account=account)
    item_ids = request.GET.getlist('item_id')
    items = []
    total = 0
    for id in item_ids:
        item = ItemInCart.objects.get(id = id)
        total += item.total_price
        items.append(item)

   

    address_id = request.GET['address']
    address = ReceiveAddress.objects.get(id=address_id)
    payment_id = request.GET['payment']
    payment = Payment.objects.get(id=payment_id)
    ship_id = request.GET['ship']
    ship = Shipment.objects.get(id=ship_id)
    amount = len(item_ids)
    total += ship.price

    info = InforOrder(customer=customer,ship=ship,payment=payment,amount=amount,total=total,receive_address=address)

    return render(request,"order.html",{'items':items,'info':info})

def payment(request):
    account = request.user
    customer = Customer.objects.get(account=account)
    item_ids = request.GET.getlist('item_id')
    items = []
    total = 0
    for id in item_ids:
        item = ItemInCart.objects.get(id = id)
        total += item.total_price
        items.append(item)

   

    address_id = request.GET['address']
    address = ReceiveAddress.objects.get(id=address_id)
    payment_id = request.GET['payment']
    payment = Payment.objects.get(id=payment_id)
    ship_id = request.GET['ship']
    ship = Shipment.objects.get(id=ship_id)
    amount = len(item_ids)
    total += ship.price

    info = InforOrder(customer=customer,ship=ship,payment=payment,amount=amount,total=total,receive_address=address)
    info.save()

    for item1 in items:
        item1.status = 0
        item1.order = info
        item1.save()

    return render(request,"payment.html")


def comment(request,product_id):
    account = request.user
    customer = Customer.objects.get(account=account)
    product = Product.objects.get(id=product_id)
    comment = request.GET['comment']
    Comment.objects.create(customer=customer,product=product,content=comment)
    return redirect("/products/detail/"+ str(product_id))

def rating(request,product_id):
    product = Product.objects.get(id=product_id)
    account = request.user
    customer = Customer.objects.get(account=account)
    Rating.objects.create(customer=customer,product=product)
    rate = request.GET['rating']
    love = Loves.objects.get(product=product)
    if(rate == "one"):
        love.one = love.one + 1
        love.save()
    elif(rate == "two"):
        love.two = love.two + 1
        love.save()
    elif(rate == "three"):
        love.three = love.three + 1
        love.save()
    elif(rate == "fore"):
        love.fore = love.fore + 1
        love.save()
    else:
        love.five = love.five + 1
        love.save()
        
    return redirect("/products/detail/"+ str(product_id))

def chat(request):
    content_customer = request.GET['content']
    account = request.user
    customer = Customer.objects.get(account=account)
    Chat.objects.create(content_customer=content_customer,customer=customer)
    return redirect('home')




