# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200, db_index=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Manufacture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200, db_index=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Название', max_length=200, db_index=True)),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(verbose_name='Изображение', blank=True, upload_to='products/%Y/%m/%d')),
                ('description', models.TextField(verbose_name='Описание', blank=True)),
                ('price', models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)),
                ('stock', models.PositiveIntegerField(verbose_name='Количество')),
                ('available', models.BooleanField(verbose_name='В наличии', default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(verbose_name='Категория', related_name='products', to='shop.Category')),
                ('manufacture', models.ForeignKey(verbose_name='Производитель', related_name='products', to='shop.Manufacture')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set([('id', 'slug')]),
        ),
    ]
