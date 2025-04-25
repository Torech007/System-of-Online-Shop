from django.shortcuts import render
from .models import Category, Product
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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
    if request.method == 'POST':
        form = UserCreationForm(request.POST) 
        if form.is_valid():
            form.save() 
            return redirect('login')  
    else:
        form = UserCreationForm()  

    return render(request, 'register.html', {'form': form})  


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # или куда тебе надо
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')