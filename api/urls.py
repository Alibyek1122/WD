from django.urls import path
from api import views

urlpatterns = [
    # categories
    path('categories/', views.CategoryListAPIView.as_view()),
    path('categories/<int:id>/', views.CategoryDetailAPIView.as_view()),
    
    # ТУХАЙН АНГИЛЛЫН БАРААНУУДЫГ ХАРАХ (Lab 10 нэмэлт)
    path('categories/<int:id>/products/', views.CategoryProductsAPIView.as_view()),

    # products
    path('products/', views.ProductListAPIView.as_view()),
    path('products/<int:product_id>/', views.ProductDetailAPIView.as_view()),
]