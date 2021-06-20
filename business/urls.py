from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='business'),
    path('upload/image',views.upload,name='upload'),
    path('delete/image/<int:image_id>',views.delete,name='delete_image'),
    path('delete/discount/<int:discount_id>',views.delete_discount,name='delete_discount'),
    path('add/discount/<int:discount_id>/<int:product_id>',views.add_discount,name='add_discount'),
    path('discount/add',views.discount_add,name='discount_add'),
    

]
