
from django.contrib import admin
from .models import Category, Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('id','name', 'price', 'count', 'display_is_active', 'category')

    def display_is_active(self, obj):
        return str(obj.is_active)
    
    display_is_active.short_description = 'Is Active'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

