from django.urls import path,include
from rest_framework.routers import DefaultRouter
from product.views import ProductViewSets,CategoryViewSet

router = DefaultRouter()
router.register('products',ProductViewSets)
router.register('categories',CategoryViewSet)

# urlpatterns = router.urls

urlpatterns = [
    path('',include(router.urls)),
]
