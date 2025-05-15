from django.urls import path
from product import views

urlpatterns = [
    path('',views.CategoryList.as_view(),name='view-categories'),
    path('<int:pk>/',views.CategoryDetails.as_view(),name="view-specific-category")
]