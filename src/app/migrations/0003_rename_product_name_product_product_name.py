# Generated by Django 5.1.1 on 2024-10-19 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_category_product_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Product_name',
            new_name='product_name',
        ),
    ]
