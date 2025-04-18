from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/category/<int:category_id>/', views.category_products, name='category_products'),
    path('cart/', views.cart, name='cart'),
    path('register/', views.register, name='register'),
]

