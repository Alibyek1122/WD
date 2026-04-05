from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # Категория ішіндегі өнімдерді алу үшін custom action
    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        category = self.get_object()
        products = category.products.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# from django.http import JsonResponse
# from .models import Category, Product
# from django.shortcuts import get_object_or_404

# def product_list(request):
#     products = Product.objects.all()
#     data = {'products': list(products.values())}
#     return JsonResponse(data, safe=False)

# def product_detail(request, id):
#     product = get_object_or_404(Product, id=id)
#     data = {
#         'id': product.id,
#         'name': product.name,
#         'price': product.price,
#         'description': product.description,
#         'count': product.count,
#         'is_active': product.is_active
#     }
#     return JsonResponse(data)

# def category_list(request):
#     categories = Category.objects.all()
#     data = {'categories': list(categories.values())}
#     return JsonResponse(data, safe=False)

# def category_detail(request, id):
#     category = get_object_or_404(Category, id=id)
#     data = {'id': category.id, 'name': category.name}
#     return JsonResponse(data)

# def category_products(request, id):
#     category = get_object_or_404(Category, id=id)
#     products = category.products.all()
#     data = {'products': list(products.values())}
#     return JsonResponse(data, safe=False)