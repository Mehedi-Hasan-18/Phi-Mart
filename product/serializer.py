from rest_framework import serializers
from decimal import Decimal
from product.models import Category,Product

# class CategorySerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     description = serializers.CharField()

# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     unit_price = serializers.DecimalField(max_digits=10,decimal_places=2,source= 'price')
#     price_with_tax = serializers.SerializerMethodField(method_name='claculate_tax')
#     # category = CategorySerializer()  #FOR SHOWING THE DATA 
    
#     #FOR SHOWING LINK AND ALSO NEED TO ADD context= {'request':request} IN THE MAIN(Product) MODEL VIEW
#     category = serializers.HyperlinkedRelatedField(
#         queryset = Category.objects.all(),
#         view_name = 'view-specific-category'
#     )
    
#     def claculate_tax(self,product):
#         return round(product.price * Decimal(1.1),2)


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
