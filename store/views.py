from django.shortcuts import render,redirect
from user.models import *


# Create your views here.

def index(request):
    orders = InforOrder.objects.filter(status=1)
    books = Store.objects.filter(product__type__icontains="Book")
    clothes = Store.objects.filter(product__type__icontains="Clothes")
    electronic = Store.objects.filter(product__type__icontains="Electronic")
    suppliers = Supplier.objects.all()
    bills = BillStore.objects.all()
    
    return render(request,"store/table.html",{'orders':orders,'books':books,'clothes':clothes,'electronic':electronic,'suppliers':suppliers,'bills':bills})

def confirm(request,order_id):
    order = InforOrder.objects.get(id=order_id)
    order.status = 2
    order.statusstr = 'đang giao hàng'
    order.save()
    return redirect("store")

def add_product(request):
    product_id = request.GET['product_id']
    product = Product.objects.get(id=product_id)
    supplier_id = request.GET['supplier_id']
    supplier =  Supplier.objects.get(id=supplier_id)
    amount = request.GET['amount']
    BillStore.objects.create(product=product,supplier=supplier,amount=amount)
    store = Store.objects.get(product__id=product_id)
    store.amount += float(amount)
    store.save()
    return redirect("store")
   






