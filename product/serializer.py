from rest_framework import serializers
from decimal import Decimal
from product.models import Category,Product

#------------------MODEL SERIALIZER-----------------------
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =['id','name','description','product_count']
        
    product_count = serializers.IntegerField()
    
class SimpleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =['id','name','description']
        
    

    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','description','price','stock','created_at','updated_at','price_with_tax','category']
        
    # category = SimpleCategorySerializer()
    price_with_tax = serializers.SerializerMethodField(method_name='claculate_tax')
    
    def claculate_tax(self,product):
        return round(product.price * Decimal(1.1),2)
