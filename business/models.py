from django.db import models
from user.models import *

# Create your models here.
class BookImageDiscount():
    product = Product()
    images = []
    discounts = []