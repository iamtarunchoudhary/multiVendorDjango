from django.urls import path
from .views import VendorView, VendorDetailView

app_name = "vendors"


urlpatterns = [
    path('vendors/', VendorView.as_view()),
    path('vendor/<pk>/', VendorDetailView.as_view()),

]




