# Create your models here.
from django.db import models

from companies.models import Company

from core.enums.retail_chain_enums import StatusOfProduct
from core.validators import check_lengh_of_product, check_date


class Product(models.Model):
    name = models.CharField(validators=[check_lengh_of_product], max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=255,
        choices=StatusOfProduct.choices,
        default=StatusOfProduct.Available
    )
    company = models.ForeignKey(Company, related_name='products', on_delete=models.CASCADE, null=True)
    date = models.DateField(validators=[check_date], null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    age = models.IntegerField()
    addition_info = models.TextField(blank=True)
    company = models.ForeignKey(Company, related_name='emploies', on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name']
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
