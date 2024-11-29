from idlelib.rpc import request_queue

from django.shortcuts import render, redirect, get_object_or_404
from Productos import forms
from Productos import models
from Productos.forms import BrandForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count



# Create your views here.

#BRANDS
@login_required
def brands(request):
    items = models.Brand.objects.all()
    return render(request, 'brands.html', {'brands' : items})

@login_required
def create_brand(request):

    if request.method == 'GET':
        return render(request, 'create_brands.html', {
            'form': forms.BrandForm
        })
    else:
        try:
            form = forms.BrandForm(request.POST)
            form.save()
            return redirect('brands')
        except ValueError:
            return render(request, 'create_brands.html', {
                'form': forms.BrandForm,
                'error': 'Por favor envie datos validos',
            })

@login_required
def detail_brand(request, id):
    if request.method == 'GET':
        brand = get_object_or_404(models.Brand, pk=id)
        form = BrandForm(instance=brand)
        return render(request, 'brand.html', {'brand': brand, 'form': form})
    else:
        try:
            brand = get_object_or_404(models.Brand, pk=id)
            form = BrandForm(request.POST, instance=brand)
            form.save()
            return redirect('brands')
        except ValueError:
            return render(request, 'brand.html', {'brand': brand, 'form': form, 'error' : "Error actualizando"})

@login_required
def delete_brand(request, id):
    brand = get_object_or_404(models.Brand, pk=id)
    if request.method == 'POST':
        brand.delete()
        return redirect('brands')

#PRODUCTS
@login_required
def products(request):
    items = models.Product.objects.all()
    return render(request, 'products.html', {'products' : items})

@login_required
def create_product(request):
    if request.method == 'GET':
        brands = models.Brand.objects.all()
        return render(request, 'create_product.html', {
            'form': forms.ProductForm,
            'brands' : brands,
        })
    else:
        try:
            form = forms.ProductForm(request.POST)
            form.save()
            return redirect('products')
        except ValueError:
            return render(request, 'create_product.html', {
                'form': forms.ProductForm,
                'error' : 'Error al enviar datos',
            })


@login_required
def detailt_product(request, id):
    if request.method == 'GET':
        product = get_object_or_404(models.Product, pk=id)
        brands = models.Brand.objects.all()
        form = forms.ProductForm(instance=product)
        return render(request, 'product.html', {'product' : product, 'form': form, 'brands' : brands})
    else:
        try:
            product = get_object_or_404(models.Product, pk=id)
            form = forms.ProductForm(request.POST, instance=product)
            form.save()
            return redirect('products')
        except ValueError:
            return render(request, 'product.html', {'product': product, 'form': form, 'error' : 'Error al actualizar'})

@login_required
def delete_product(request, id):
    product = get_object_or_404(models.Product, pk=id)
    if request.method == 'POST':
        product.delete()
        return redirect('products')

@login_required
def stats(request):
    # Agrupar los productos por la marca y contar cuantos hay por cada una
    product_counts = models.Product.objects.values('brand_id__name').annotate(product_count=Count('id')).order_by('-product_count')

    # Extraer los nombres de las marcas y la cantidad de productos
    brand_names = [item['brand_id__name'] for item in product_counts]
    product_counts_data = [item['product_count'] for item in product_counts]

    return render(request, 'statistics.html', {
        'brand_names': brand_names,
        'product_counts_data': product_counts_data
    })


def game(request):
    return render(request, 'game.html')


