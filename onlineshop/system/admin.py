from django.contrib import admin
from .models import catalog, Category, Product

@admin.register(catalog)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',) 
    list_filter = ('created_at',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    search_fields = ('name', 'description')
    list_filter = ('category', 'price')    