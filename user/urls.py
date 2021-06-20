from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('login',views.user_login,name='login'),
    path('cart',views.cart,name='cart'),
    path('products/detail/<int:product_id>',views.product_detail,name="product_detail"),
    path('products/clothes>',views.clothes,name="clothes"),
    path('products/book>',views.book,name="book"),
    path('products/electronic>',views.electronic,name="electronic"),
    path('cart/add_to_cart/<int:product_id>',views.order,name='order'),
    path('cart/delete/<int:item_id>',views.deleteincart,name='deleteincart'),
    path('cart/payment_confirm',views.paymentconfirm,name='paymentConfirm'),
    path('cart/payment',views.payment,name='payment'),
    path('cart/comment/<int:product_id>',views.comment,name='comment'),
    path('cart/product/rating/<int:product_id>',views.rating,name='rating'),
    path('chat/',views.chat,name='chat'),
    path('product/search',views.search,name='search'),


   

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)