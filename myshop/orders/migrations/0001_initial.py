# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('first_name', models.CharField(verbose_name='Имя', max_length=50)),
                ('last_name', models.CharField(verbose_name='Фамилия', max_length=50)),
                ('email', models.EmailField(verbose_name='E-mail', max_length=254)),
                ('address', models.CharField(verbose_name='Адресс', max_length=250)),
                ('postal_code', models.CharField(verbose_name='Почтовый код', max_length=20)),
                ('city', models.CharField(verbose_name='Город', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(verbose_name='Оплачено', default=False)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('price', models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество', default=1)),
                ('order', models.ForeignKey(verbose_name='Заказ', related_name='items', to='orders.Order')),
                ('product', models.ForeignKey(verbose_name='Товар', related_name='order_items', to='shop.Product')),
            ],
        ),
    ]
