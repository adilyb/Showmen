# Generated by Django 5.0 on 2024-01-04 15:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['category_name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=150, unique=True)),
                ('product_desc', models.CharField(max_length=250, unique=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.productcategory')),
            ],
        ),
    ]
