from rest_framework import serializers
from .models import Vendors, Products 


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendors
        fields = '__all__'


# class ProductSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Products
#         fields = '__all__'