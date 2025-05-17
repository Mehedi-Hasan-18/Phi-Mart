from django.urls import path,include
from rest_framework.routers import DefaultRouter
from product.views import ProductViewSets,CategoryViewSet,ReviewViewSet
from rest_framework_nested import routers
from order.views import CartViewSet,CartItemViewSet

router = routers.DefaultRouter()
router.register('products',ProductViewSets)
router.register('categories',CategoryViewSet)
router.register('carts',CartViewSet,basename='carts')

product_router = routers.NestedDefaultRouter(router,'products', lookup='product')
product_router.register('review',ReviewViewSet,basename='product-review')

cart_router = routers.NestedDefaultRouter(router,'carts',lookup='cart')
cart_router.register('items',CartItemViewSet,basename='cart-item')

# urlpatterns = router.urls

urlpatterns = [
    path('',include(router.urls)),
    path('',include(product_router.urls)),
    path('',include(cart_router.urls)),
]
