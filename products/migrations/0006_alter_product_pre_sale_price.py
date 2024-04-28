# Generated by Django 3.2 on 2024-04-27 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_pre_sale_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pre_sale_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]