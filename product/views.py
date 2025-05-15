from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product,Category
from product.serializer import ProductSerializer,CategorySerializer
from django.db.models import Count
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

class ProductList(ListCreateAPIView):
    queryset = Product.objects.select_related("category").all()
    serializer_class = ProductSerializer
    
class ProductDetails(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

class CategoryList(ListCreateAPIView):
    queryset = Category.objects.annotate(product_count = Count("products")).all()
    serializer_class = CategorySerializer

class CategoryDetails(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.annotate(product_count = Count("products")).all()
    serializer_class = CategorySerializer
