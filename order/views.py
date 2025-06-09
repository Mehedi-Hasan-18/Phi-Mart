from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,DestroyModelMixin
from order.models import Cart,CartItem,Order,OrderItem
from order.serializer import CartSerializer,CartItemSerializer,AddCartItemSerializer,UpdateCartItemSerializer,CreateOrderSerializer,OrderItemSerializer,OrderSerializer,UpdateOrderSerializer,EmptySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action
from order import services
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class CartViewSet(CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        if Cart.objects.filter(user=self.request.user).exists():
            raise ValidationError("You already have a cart.")
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Cart.objects.none() 
        return Cart.objects.filter(user = self.request.user)
    
    def create(self,request,*args,**kwargs):
        existing_data = Cart.objects.filter(user = self.request.user).first()
        
        if existing_data:
            serializer = self.get_serializer(existing_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return super().create(request,*args,**kwargs)
    
    
class CartItemViewSet(ModelViewSet):
    http_method_names = ['get','post', 'patch','delete']
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        return CartItemSerializer
    
    def get_serializer_context(self):
        if getattr(self, 'swagger_fake_view', False):
            return {}
        return {'cart_id':self.kwargs['cart_pk']}
    
    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return CartItem.objects.none() 
        return CartItem.objects.filter(cart_id = self.kwargs['cart_pk'])
    
class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    http_method_names = ['get','post','patch','delete','head','option']
    
    @action(detail=True,methods=['post'])
    def cancel(self,request,pk=None):
        order = self.get_object()
        services.OrderServices.canceled_order(order=order,user=request.user)
        return Response({"status":"Your Order is Canceled"})
    
    @action(detail=True,methods=['patch'])
    def update_status(self,request,pk=None):
        order = self.get_object()
        serializer = UpdateOrderSerializer(order, data = request.data, partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"status":f"status Change To {request.data['status']}"})
    
    def get_permissions(self):
        if self.action in ['update_status','destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]
    
    def get_serializer_class(self):
        if self.action == 'cancel':
            return EmptySerializer
        if self.action == 'create':
            return CreateOrderSerializer
        if self.action == 'update_status':
            return UpdateOrderSerializer
        return OrderSerializer
    def get_queryset(self):
        # Handle schema generation (DRF-YASG)
        if getattr(self, 'swagger_fake_view', False):
            return Order.objects.none()  # Return empty queryset for schema 
        
        # Staff users see all orders
        if self.request.user.is_staff:
            return Order.objects.prefetch_related('items__product').all()
        return Order.objects.prefetch_related('items__product').filter(user=self.request.user)

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return CartItem.objects.none() 
        
        if self.request.user.is_staff == True:
            return Order.objects.prefetch_related('items__product').all()
        return Order.objects.prefetch_related('items__product').filter(user = self.request.user)
    
    def get_serializer_context(self):
        return {'user_id':self.request.user.id,'user':self.request.user}
