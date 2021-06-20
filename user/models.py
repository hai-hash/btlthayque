from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Category(models.Model):
    name = models.CharField(max_length=100,default='')
class Author(models.Model):
    name = models.CharField(max_length=100,default='')

class Material(models.Model):
    name = models.CharField(max_length=100,default='')
class Brand(models.Model):
    name = models.CharField(max_length=100,default='')
class Types(models.Model):
    name = models.CharField(max_length=100,default='')

class Color(models.Model):
    name_color = models.CharField(max_length=100,default='')
    code_color = models.CharField(max_length=100,default='')

class FullName(models.Model):
    first_name = models.CharField(max_length=100,default='')
    last_name = models.CharField(max_length=100,default='')

class Address(models.Model):
    city = models.CharField(max_length=100,default='')
    district = models.CharField(max_length=100,default='')
    villate = models.CharField(max_length=100,default='')
    number_house = models.CharField(max_length=100,default='')

class Customer(models.Model):
    email = models.CharField(max_length=100,default='')
    number_phone = models.CharField(max_length=100,default='')
    full_name = models.ForeignKey(FullName,on_delete=models.CASCADE)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    account = models.ForeignKey(User,on_delete=models.CASCADE)

class Product(models.Model):
    name_product = models.CharField(max_length=100,default='')
    price = models.FloatField(default=0)
    image_main_product = models.ImageField()
    describe = models.TextField(default='sản phẩm này rất sịn sò')
    type = models.CharField(max_length=100,default='defau')
    def __str__(self):
        return self.name_product
    
class Product_Color(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)

class Image(models.Model):
    path_image = models.ImageField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE,default='')
    

class Book(Product):
    category =  models.ForeignKey(Category,on_delete=models.CASCADE,default='')
    author =  models.ForeignKey(Author,on_delete=models.CASCADE,default='')
    

class Size(models.Model):
    value = models.CharField(max_length=100,default='')
   

class Clothes(Product):
    material = models.ForeignKey(Material,on_delete=models.CASCADE,default='')
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,default='')
    

class Supplier(models.Model):
    name = models.CharField(max_length=100,default='')
    email = models.CharField(max_length=100,default='')
    number_phone = models.CharField(max_length=100,default='')
    address = models.CharField(max_length=100,default='')
    
class Electronic(Product):
    types = models.ForeignKey(Types,on_delete=models.CASCADE,default='')

class Discount(models.Model):
    name = models.CharField(max_length=100,default='')
    code = models.CharField(max_length=100,default='')
    value = models.FloatField(default=0)
    phantram = models.IntegerField(default=0)
    max_value = models.FloatField(default=0)
    min_price = models.FloatField(default=0)
    status = models.IntegerField(default=1)
    def __str__(self):
        return self.name
   

class Product_Discount(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,default='')
    discount = models.ForeignKey(Discount,on_delete=models.CASCADE,default='')
    status = models.IntegerField(default=1)

class Shipment(models.Model):
    name = models.CharField(max_length=100,default='')
    price = models.FloatField(default=0)

class Payment(models.Model):
    name = models.CharField(max_length=100,default='')







class ReceiveAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,default='')
    city = models.CharField(max_length=100,default='')
    district = models.CharField(max_length=100,default='')
    villate = models.CharField(max_length=100,default='')
    number_house = models.CharField(max_length=100,default='')
    number_phone = models.CharField(max_length=100,default='')

class InforOrder(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,default='')
    orderDate = models.DateField(blank=True,null=True,default=datetime.now)
    ship = models.ForeignKey(Shipment,on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    receiveDate = models.DateField(default=datetime.now,blank=True)
    amount = models.IntegerField(default=0)
    total = models.FloatField(default=0)
    statusstr = models.CharField(max_length=100,default='đang chờ xác nhận')
    process = models.IntegerField(default=25)
    receive_address = models.ForeignKey(ReceiveAddress,on_delete=models.CASCADE,default='')
    def __str__(self):
        return str(self.id)
    

class ItemInCart(models.Model):
    account = models.ForeignKey(User,on_delete=models.CASCADE,default='')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    color = models.CharField(max_length=20,default='default color')
    size = models.CharField(max_length=20,default='default size')
    total = models.FloatField(default=0)
    total_price = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    status = models.IntegerField(default=1)
    order = models.ForeignKey(InforOrder,on_delete=models.CASCADE,default='')

class Comment(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,default='')
    content = models.TextField(default='')

class Loves(models.Model):
    one = models.IntegerField(default=0)
    two = models.IntegerField(default=0)
    three = models.IntegerField(default=0)
    fore = models.IntegerField(default=0)
    five = models.IntegerField(default=0)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

class Rating(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,default='')
    status = models.IntegerField(default=0)

class Chat(models.Model):
    content_customer = models.TextField(default='')
    content_admin = models.TextField(default='')
    status = models.IntegerField(default=0)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,default='')

class Store(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,default='')
    amount = models.FloatField(default=0)
    import_price = models.FloatField(default=0)

class BillStore(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,default='')
    amount = models.FloatField(default=0)
    import_date = models.DateField(blank=True,null=True,default=datetime.now)
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE)



class Order():
    order = InforOrder()
    list_item = []

class Messeage():
    account = User()
    list_chat = []
    status = 0
    last_message = Chat()

    






    



class Order_Item(models.Model):
    infoorder = models.ForeignKey(InforOrder,on_delete=models.CASCADE)
    item = models.ForeignKey(ItemInCart,on_delete=models.CASCADE)
   


