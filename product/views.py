from product.models import Product,Category
from product.serializer import ProductSerializer,CategorySerializer
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet

class ProductViewSets(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(product_count = Count("products")).all()
    serializer_class = CategorySerializer

