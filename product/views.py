from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product,Category
from product.serializer import ProductSerializer,CategorySerializer
from django.db.models import Count
from rest_framework import status

@api_view(['GET','POST'])
def view_products(request):
    if request.method =='GET':
        products = Product.objects.select_related("category").all()
        serializer = ProductSerializer(products,many= True)
        return Response(serializer.data)
    if request.method == 'POST':
        #Deserializer
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)   #raise_exception works like if and else in one
        serializer.save()
        return Response(serializer.data,status=status.HTTP_404_NOT_FOUND)


@api_view(['GET','PUT','DELETE'])
def view_specific_product(request,id):
    if request.method == 'GET':
        product = get_object_or_404(Product,pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(product)
    
    if request.method == 'DELETE':
        product = get_object_or_404(Product,pk=id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view()
def view_categories(request):
    categories = Category.objects.annotate(product_count = Count('products')).all()
    serializer = CategorySerializer(categories,many= True)
    return Response(serializer.data)

@api_view()
def view_specific_category(request,pk):
    category = get_object_or_404(Category.objects.annotate(product_count=Count('products')), pk=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)
