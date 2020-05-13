from django.db import models
from django.core.urlresolvers import reverse
from PIL import Image

class Category(models.Model):

    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])

class Manufacture(models.Model):

    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_manufacture',
                       args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', related_name='products')
    manufacture = models.ForeignKey(Manufacture, verbose_name='Производитель', related_name='products')
    name = models.CharField("Название", max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField("Изображение", upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField("Описание", blank=True)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField("Количество")
    available = models.BooleanField("В наличии", default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])

