from django.urls import path,include
from product.views import ProductViewSets,CategoryViewSet,ReviewViewSet,ProductImageViewSet
from rest_framework_nested import routers
from order.views import CartViewSet,CartItemViewSet,OrderViewSet,HasOrderProduct

router = routers.DefaultRouter()
router.register('products',ProductViewSets)
router.register('categories',CategoryViewSet)
router.register('carts',CartViewSet,basename='carts')
router.register('orders',OrderViewSet,basename='orders')

product_router = routers.NestedSimpleRouter(router,'products', lookup='product')
product_router.register('review',ReviewViewSet,basename='product-review')
product_router.register('images',ProductImageViewSet, basename='product-images')

cart_router = routers.NestedSimpleRouter(router,'carts',lookup='cart')
cart_router.register('items',CartItemViewSet,basename='cart-item')

# urlpatterns = router.urls

urlpatterns = [
    path('',include(router.urls)),
    path('',include(product_router.urls)),
    path('',include(cart_router.urls)),
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.jwt')),
    path('order/has-created/<int:product_id>/',HasOrderProduct.as_view(), name='order-created')
    # path("payment/initiate",payment_initiate, name="payment-integrate")
]
