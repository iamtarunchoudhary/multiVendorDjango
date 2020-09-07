# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import uuid


class Customers(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=50)
    status = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'customers'


class Gallery(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    product_id = models.CharField(max_length=50)
    image_url = models.CharField(max_length=200)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gallery'


class Products(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    vendor_id = models.CharField(max_length=50)
    name = models.CharField(max_length=250)
    long_description = models.TextField()
    in_stocks = models.IntegerField()
    type = models.IntegerField()
    sales_price = models.CharField(max_length=10)
    status = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    updated_by = models.CharField(max_length=50)
    short_description = models.CharField(max_length=100)
    parent_id = models.CharField(max_length=50)
    category = models.IntegerField()
    sub_category = models.IntegerField()
    max_quantity_per_order = models.IntegerField()
    rating = models.IntegerField()
    backorders_allowed = models.IntegerField()
    regular_price = models.CharField(max_length=10)
    tag = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'products'


class Vendors(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    id_proof = models.CharField(max_length=200)
    image = models.CharField(max_length=200, default=None)
    password = models.CharField(max_length=200)
    status = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'vendors'
