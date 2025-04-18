from django.shortcuts import render
from .models import Category, Product

def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})

def catalog(request):
    return render(request, 'catalog.html')

def category_products(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'catalog.html', {'products': products, 'category': category})    

def cart(request):
    return render(request, 'cart.html')

def register(request):
    return render(request, 'register.html')