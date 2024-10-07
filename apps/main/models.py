from django.db import models

class Product(models.Model):
    name = models.CharField(verbose_name="Название товара", max_length=255)
    description = models.TextField(verbose_name="Описание товара", null=True, blank=True)
    price = models.DecimalField(verbose_name="Цена товара", max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
