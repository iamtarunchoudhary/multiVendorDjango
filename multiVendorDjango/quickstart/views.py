from django.shortcuts import render
from .serializers import VendorSerializer
from rest_framework.views import APIView
from .models import Vendors
from rest_framework.response import Response
from django.http import Http404



class VendorView(APIView):

    def get(self, request):
        vendors = Vendors.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response({"vendors": serializer.data})



    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            saved_vendor = serializer.save()
            return Response({"status":200, "success": "Vendor created successfully", "data": {"id": saved_vendor.id}})
        return Response({"status":400, "success": "Some thing went wrong", "data": {}})




class VendorDetailView(APIView):

    def get(self, request, pk=None):
        try:
            vendor =  Vendors.objects.get(pk=pk)
            serializer = VendorSerializer(vendor)
            return Response({"vendor": serializer.data})
        except Vendors.DoesNotExist:
            raise Http404



    





def Reactapp(request, resource=''):
    return render(request, 'quickstart/index.html')