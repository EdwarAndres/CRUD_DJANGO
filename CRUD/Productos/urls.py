from tkinter.font import names

from django.urls import path
from Productos import views

urlpatterns = [
    #Brands
    path('brands/', views.brands, name='brands'),
    path('brand/create', views.create_brand, name='brand_create'),
    path('brand/<int:id>', views.detail_brand, name='detail_brand'),
    path('brand/<int:id>/delete', views.delete_brand, name='delete_brand'),

    #Products
    path('products/', views.products, name='products'),
    path('product/create', views.create_product, name='product_create'),
    path('product/<int:id>', views.detailt_product, name='detail_product'),
    path('product/<int:id>/delete', views.delete_product, name='delete_product'),

    #Statics
    path('stats/', views.stats, name='stats')
]