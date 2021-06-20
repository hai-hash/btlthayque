from django.shortcuts import redirect, render
from user.models import *
from .models import *

# Create your views here.
def index(request):
    books = Book.objects.all()
    clothes = Clothes.objects.all()
    electronics = Electronic.objects.all()
    list_discount = Discount.objects.all()
    books1 = []
    clothes1 = []
    electronics1 = []
    for book in books :
        book_image_discount = BookImageDiscount()
        book_image_discount.product = book
        images = Image.objects.filter(product=book)
        book_image_discount.images = images
        discounts = Product_Discount.objects.filter(product=book)
        book_image_discount.discounts = discounts
        books1.append(book_image_discount)
    
    for clothe in clothes :
        book_image_discount = BookImageDiscount()
        book_image_discount.product = clothe
        images = Image.objects.filter(product=clothe)
        book_image_discount.images = images
        discounts = Product_Discount.objects.filter(product=clothe)
        book_image_discount.discounts = discounts
        clothes1.append(book_image_discount)

    for electronic in electronics :
        book_image_discount = BookImageDiscount()
        book_image_discount.product = electronic
        images = Image.objects.filter(product=electronic)
        book_image_discount.images = images
        discounts = Product_Discount.objects.filter(product=electronic)
        book_image_discount.discounts = discounts
        electronics1.append(book_image_discount)


   
    return render(request,"busi/table.html",{'books1':books1,'clothes':clothes1,'electronics':electronics1,'discounts':list_discount})

def upload(request):
    product_id = request.POST['product_id']
    product = Product.objects.get(id=product_id)
    image = request.FILES['image']
    Image.objects.create(product=product,path_image=image)
    return redirect('business')

def delete(request,image_id):
    image = Image.objects.get(id=image_id).delete()
    return redirect('business')

def delete_discount(request,discount_id):
    Product_Discount.objects.get(id=discount_id).delete()
    return redirect('business')

def add_discount(request,discount_id,product_id):
    product = Product.objects.get(id=product_id)
    discount = Discount.objects.get(id=discount_id)
    Product_Discount.objects.create(product=product,discount=discount)
    return redirect('business')

def discount_add(request):
    name = request.GET['name']
    code = request.GET['code']
    value = request.GET['value']
    phantram = request.GET['phantram']
    Discount.objects.create(name=name,code=code,value=value,phantram=phantram)
    return redirect('business')


