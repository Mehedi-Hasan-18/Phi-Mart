from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product,Category
from product.serializer import ProductSerializer,CategorySerializer
from django.db.models import Count
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView


class ViewProduct(APIView):
    def get(self,request):
        product = Product.objects.select_related("category").all()
        serializer = ProductSerializer(product, many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ProductSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
    
#ALL WORK OF ViewProduct
class ProductList(ListCreateAPIView):
    queryset = Product.objects.select_related("category").all()
    serializer_class = ProductSerializer
    
class ProductDetails(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    #WE CAN OVERWRITE SOME METHOD FOR OUR NEEDS
    
class ViewSpecificProduct(APIView):
    def get(self,request,id):
        product = get_object_or_404(Product,pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self,request,id):
        product = get_object_or_404(Product,pk=id)
        serializer = ProductSerializer(product,data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self,request,id):
        product = get_object_or_404(Product,pk=id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ViewCategory(APIView):
    def get(self,request):
        categories = Category.objects.annotate(product_count = Count("products")).all()
        serializer = CategorySerializer(categories,many= True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = CategorySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class CategoryList(ListCreateAPIView):
    queryset = Category.objects.annotate(product_count = Count("products")).all()
    serializer_class = CategorySerializer

class CategoryDetails(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.annotate(product_count = Count("products")).all()
    serializer_class = CategorySerializer

class ViewSpecificCategory(APIView):
    def get(self,request,pk):
        category = get_object_or_404(Category.objects.annotate(product_count=Count('products')), pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self,request,pk):
        category = category = get_object_or_404(Category.objects.annotate(product_count=Count('products')), pk=pk)
        serializer = CategorySerializer(category,data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self,request,pk):
        category = category = get_object_or_404(Category.objects.annotate(product_count=Count('products')), pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

