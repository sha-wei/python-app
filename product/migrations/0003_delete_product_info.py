# Generated by Django 2.1.2 on 2018-10-07 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_info'),
    ]

    operations = [
        migrations.DeleteModel(
            name='product_info',
        ),
    ]
