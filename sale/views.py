from django.shortcuts import render,redirect
from user.models import *;


# Create your views here.

def index(request):
    items = ItemInCart.objects.all()
    orders = InforOrder.objects.filter(status=0)
    accounts = User.objects.all()
    List_user_chat = []
    dem = 0
    for account in accounts:
        chats = Chat.objects.filter(customer__account=account)
        if len(chats) != 0:
            messeage = Messeage()
            messeage.account = account
            messeage.list_chat = chats
            messeage.last_message = chats.last()
            for chat in chats:
                if(chat.status == 0):
                    messeage.status = 1
            if messeage.status == 1:
                dem = dem + 1
            List_user_chat.append(messeage)
        

    return render(request,"sale/table.html",{'items':items,'orders':orders,'messages':List_user_chat,'dem':dem})

def confirm(request,order_id):
    order = InforOrder.objects.get(id=order_id)
    order.status = 1
    order.statusstr = 'đang chờ lấy hàng'
    order.save()
    return redirect("sale")

def chat(request):
    content = request.GET['content']
    account_id = request.GET['account_id']
    account = User.objects.get(id=account_id)
    customer = Customer.objects.get(account=account)
    Chat.objects.create(customer=customer,content_admin=content,status=1)
    chats = Chat.objects.filter(customer__account=account)
    for chat in chats:
        if chat.status == 0:
            chat.status = 1
            chat.save
    return redirect("sale")

