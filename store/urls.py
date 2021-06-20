from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='store'),
    path('comfirm/<int:order_id>',views.confirm,name='store_comfirm'),
    path('add/product',views.add_product,name='add_product'),


]
