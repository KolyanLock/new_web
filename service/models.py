from django.db import models


# Create your models here.

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    cost = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)
    is_active = models.BooleanField(verbose_name='Активен', default=True, null=True)

    def __str__(self):
        return self.title


class Bin(models.Model):
    id = models.IntegerField(primary_key=True)
    cost = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title


class Home(models.Model):
    size = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Размер', null=True)
    cost = models.IntegerField(verbose_name='Цена', null=True)
    adr = models.CharField(max_length=200, verbose_name='Адрес', default='Планета Земля')
    bal = models.BooleanField(verbose_name='Балкон', default=True)

    def __str__(self):
        return self.adr
