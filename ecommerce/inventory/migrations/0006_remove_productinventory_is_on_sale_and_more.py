# Generated by Django 4.1.7 on 2023-05-06 07:00

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0005_productinventory_is_digital_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="productinventory",
            name="is_on_sale",
        ),
        migrations.RemoveField(
            model_name="productinventory",
            name="sale_price",
        ),
        migrations.AlterField(
            model_name="productinventory",
            name="retail_price",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=7,
                validators=[django.core.validators.MinValueValidator(Decimal("0.01"))],
                verbose_name="Recommended Retail Price",
            ),
        ),
    ]
