# Generated by Django 4.1.7 on 2023-05-06 13:03

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("inventory", "0006_remove_productinventory_is_on_sale_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Coupon",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120)),
                ("coupon_code", models.CharField(max_length=23)),
            ],
        ),
        migrations.CreateModel(
            name="ProductOnPromotion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "promo_price",
                    models.DecimalField(
                        decimal_places=2,
                        default=Decimal("0.00"),
                        max_digits=7,
                        validators=[
                            django.core.validators.MinValueValidator(Decimal("0.00"))
                        ],
                    ),
                ),
                ("price_override", models.BooleanField(default=False)),
                (
                    "product_inventory_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="product_inventory",
                        to="inventory.productinventory",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PromoType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name="Promotion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120, unique=True)),
                ("description", models.TextField(blank=True)),
                ("promo_reduction", models.IntegerField()),
                ("is_active", models.BooleanField(default=False)),
                ("is_schedule", models.BooleanField(default=False)),
                ("promo_start", models.DateField()),
                ("promo_end", models.DateField()),
                (
                    "coupon",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="coupon",
                        to="promotion.coupon",
                    ),
                ),
                (
                    "product_on_promotion",
                    models.ManyToManyField(
                        related_name="products_on_promotion",
                        through="promotion.ProductOnPromotion",
                        to="inventory.productinventory",
                    ),
                ),
                (
                    "promo_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="promo_type",
                        to="promotion.promotype",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="productonpromotion",
            name="promotion_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Promotion",
                to="promotion.promotion",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="productonpromotion",
            unique_together={("product_inventory_id", "promotion_id")},
        ),
    ]
