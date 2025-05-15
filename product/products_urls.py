from django.urls import path
from product import views

urlpatterns = [
    path('',views.ProductList.as_view(), name="view-products"),
    path('<int:id>/',views.ProductDetails.as_view(),name='view_specific_product')
]
