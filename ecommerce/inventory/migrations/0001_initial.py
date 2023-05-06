# Generated by Django 4.1.7 on 2023-03-28 05:40

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Brand",
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
                    "name",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Brand Name"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Category",
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
                    "name",
                    models.CharField(
                        help_text="format:required , max-100",
                        max_length=100,
                        verbose_name="category name",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="format : required  letters,numbers,underscore or hyphens",
                        max_length=150,
                        verbose_name="category safe url",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("lft", models.PositiveIntegerField(editable=False)),
                ("rght", models.PositiveIntegerField(editable=False)),
                ("tree_id", models.PositiveIntegerField(db_index=True, editable=False)),
                ("level", models.PositiveIntegerField(editable=False)),
                (
                    "parent",
                    mptt.fields.TreeForeignKey(
                        blank=True,
                        help_text="format : not required",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="children",
                        to="inventory.category",
                        verbose_name="parent of category",
                    ),
                ),
            ],
            options={
                "verbose_name": "product_category",
                "verbose_name_plural": "product_categories",
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                    "web_id",
                    models.CharField(
                        max_length=50, unique=True, verbose_name="product website Id"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        max_length=150, verbose_name="Product Name safe url"
                    ),
                ),
                ("name", models.CharField(max_length=150, verbose_name="Product name")),
                ("description", models.TextField(verbose_name="Product Description")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date Product Created"
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                ("category", mptt.fields.TreeManyToManyField(to="inventory.category")),
            ],
        ),
        migrations.CreateModel(
            name="ProductAttribute",
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
                ("name", models.CharField(max_length=255, unique=True)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="ProductAttributeValue",
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
                ("attribute_value", models.CharField(max_length=255)),
                (
                    "product_attribute",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="inventory.productattribute",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductAttributeValues",
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
                    "attributevalues",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="attributevaluess",
                        to="inventory.productattributevalue",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductInventory",
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
                    "sku",
                    models.CharField(
                        max_length=20, unique=True, verbose_name="Stock Keeping Unit"
                    ),
                ),
                (
                    "upc",
                    models.CharField(
                        max_length=12,
                        unique=True,
                        verbose_name="Universal Product Code",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("is_default", models.BooleanField(default=False)),
                (
                    "retail_price",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=7,
                        verbose_name="Recommended Retail Price",
                    ),
                ),
                (
                    "store_price",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=7,
                        verbose_name="Regular Store Price",
                    ),
                ),
                (
                    "sale_price",
                    models.DecimalField(
                        decimal_places=2, max_digits=7, verbose_name="Sale Price"
                    ),
                ),
                ("weight", models.FloatField(verbose_name="Product Weight")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date sub-product created"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="date sub-product updated"
                    ),
                ),
                (
                    "attribute_values",
                    models.ManyToManyField(
                        related_name="product_attribute_values",
                        through="inventory.ProductAttributeValues",
                        to="inventory.productattributevalue",
                    ),
                ),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="brand",
                        to="inventory.brand",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="product",
                        to="inventory.product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductType",
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
                    "name",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Product Type"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Stock",
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
                ("last_checked", models.DateTimeField(blank=True, null=True)),
                ("units", models.IntegerField(default=0)),
                ("units_sold", models.IntegerField(default=0)),
                (
                    "product_inventory",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Stock_Product_inventory",
                        to="inventory.productinventory",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="productinventory",
            name="product_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="product_type",
                to="inventory.producttype",
            ),
        ),
        migrations.AddField(
            model_name="productattributevalues",
            name="productinventory",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="productattributevaluess",
                to="inventory.productinventory",
            ),
        ),
        migrations.CreateModel(
            name="Media",
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
                    "image",
                    models.ImageField(
                        default="images/default.png",
                        upload_to="images/",
                        verbose_name="product image",
                    ),
                ),
                (
                    "alt_text",
                    models.CharField(max_length=255, verbose_name="aleternative text"),
                ),
                ("is_feature", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "product_inventory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="media_product_inventory",
                        to="inventory.productinventory",
                    ),
                ),
            ],
        ),
        migrations.AlterUniqueTogether(
            name="productattributevalues",
            unique_together={("attributevalues", "productinventory")},
        ),
    ]
