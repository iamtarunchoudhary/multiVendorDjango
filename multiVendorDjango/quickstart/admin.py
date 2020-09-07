from django.contrib import admin
from .models import Customers, Gallery, Products, Vendors

# Register your models here.

admin.site.register(Customers)
admin.site.register(Products)
admin.site.register(Gallery)
admin.site.register(Vendors)
