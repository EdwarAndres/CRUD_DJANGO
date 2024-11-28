from django.db import models

# Create your models here.


#Marcas
class Brand(models.Model):
    name = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


#Productos
class Product(models.Model):
    name = models.TextField()
    description = models.CharField(max_length=100)
    stock = models.IntegerField()
    price = models.FloatField()
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'



