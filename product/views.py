from product.models import Product,Category,Review,ProductImage
from product.serializer import ProductSerializer,CategorySerializer,ReviewSerializer,ProductImageSerializer
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from product.filters import ProductFilter
from rest_framework.filters import SearchFilter,OrderingFilter
from product.paginations import DefaulfPagination
from api.permission import IsAdminOrReadOnly
from .permission import IsAuthorOrReadOnly
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ProductViewSets(ModelViewSet):
    """
    API Endpoint for Managing Product in the e-commerce Store
    -Allow Authenticate Admin to create,update and delete product
    """
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    pagination_class = DefaulfPagination
    filterset_class = ProductFilter
    search_fields = ['name','description']
    ordering_fields = ['price','updated_at']
    permission_classes = [IsAdminOrReadOnly]
    
    def get_queryset(self):
        return  Product.objects.prefetch_related('images').all()
    
    @swagger_auto_schema(
        operation_summary='Get All Products with Filtering',
        manual_parameters=[
            openapi.Parameter(
                'category_id',
                openapi.IN_QUERY,
                description="Filter by exact category ID",
                type=openapi.TYPE_INTEGER
            ),
            openapi.Parameter(
                'price__gt',
                openapi.IN_QUERY,
                description="Filter products with price greater than this value",
                type=openapi.TYPE_NUMBER
            ),
            openapi.Parameter(
                'price__lt',
                openapi.IN_QUERY,
                description="Filter products with price less than this value",
                type=openapi.TYPE_NUMBER
            ),
            openapi.Parameter(
                'search',
                openapi.IN_QUERY,
                description="Search in product name and description",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'ordering',
                openapi.IN_QUERY,
                description="Order by: price, -price, updated_at, -updated_at",
                type=openapi.TYPE_STRING
            ),
        ]
    )
    
    def list(self, request, *args, **kwargs):
        """
        Retrive All The Product
        """
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary='Admin Can Create Product'
    )
    def create(self, request, *args, **kwargs):
        """
        Authenticate Admin can Create Product
        """
        return super().create(request, *args, **kwargs)
    
class ProductImageViewSet(ModelViewSet):
    serializer_class = ProductImageSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    def get_queryset(self):
        return ProductImage.objects.filter(product_id = self.kwargs.get('product_pk'))
    
    def perform_create(self, serializer):
        serializer.save(product_id = self.kwargs.get('product_pk'))
    
class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Category.objects.annotate(product_count = Count("products")).all()
    serializer_class = CategorySerializer
    
class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes=[IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
    
    def get_queryset(self):
        return Review.objects.filter(product_id = self.kwargs.get('product_pk'))
    
    def get_serializer_context(self):
        return {'product_id':self.kwargs.get('product_pk')}

