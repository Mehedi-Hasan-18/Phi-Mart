from django.urls import path,include
from rest_framework.routers import DefaultRouter
from product.views import ProductViewSets,CategoryViewSet,ReviewViewSet
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products',ProductViewSets)
router.register('categories',CategoryViewSet)

product_router = routers.NestedDefaultRouter(router,'products', lookup='product')
product_router.register('review',ReviewViewSet,basename='product-review')

# urlpatterns = router.urls

urlpatterns = [
    path('',include(router.urls)),
    path('',include(product_router.urls)),
]
