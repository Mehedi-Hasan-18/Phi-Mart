from product.models import Product,Category,Review
from product.serializer import ProductSerializer,CategorySerializer,ReviewSerializer
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from product.filters import ProductFilter
from rest_framework.filters import SearchFilter,OrderingFilter
from product.paginations import DefaulfPagination

class ProductViewSets(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    pagination_class = DefaulfPagination
    filterset_class = ProductFilter
    search_fields = ['name','description']
    ordering_fields = ['price','updated_at']
    
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(product_count = Count("products")).all()
    serializer_class = CategorySerializer
    
class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        return Review.objects.filter(product_id = self.kwargs['product_pk'])
    
    def get_serializer_context(self):
        return {'product_id':self.kwargs['product_pk']}

