from product.models import Product,Category,Review
from product.serializer import ProductSerializer,CategorySerializer,ReviewSerializer
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet

class ProductViewSets(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(product_count = Count("products")).all()
    serializer_class = CategorySerializer
    
class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        return Review.objects.filter(product_id = self.kwargs['product_pk'])
    
    def get_serializer_context(self):
        return {'product_id':self.kwargs['product_pk']}

