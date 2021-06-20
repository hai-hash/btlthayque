
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='sale'),
    path('comfirm/<int:order_id>',views.confirm,name='sale_comfirm'),
    path('chat/',views.chat,name="chat_sale"),
    


]
