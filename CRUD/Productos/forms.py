from django.forms import ModelForm
from Productos import models

class BrandForm(ModelForm):
    class Meta:
        model = models.Brand
        fields = ['name']

class ProductForm(ModelForm):
    class Meta:
        model = models.Product
        fields = [
            'name',
            'description',
            'stock',
            'price',
            'brand_id',
        ]