from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=60, unique=True)
    description = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Stock(models.Model):
    address = models.CharField(max_length=200, unique=True)
    products = models.ManyToManyField(Product, through='StockProduct', related_name='stocks', verbose_name='запас')
    
    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'


class StockProduct(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='positions', )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='positions', )
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=18, decimal_places=2, validators=[MinValueValidator(0)], )
    
    class Meta:
        constraints = [models.UniqueConstraint(name='unique_stock', fields=['stock', 'product'])]