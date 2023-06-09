# Generated by Django 4.1.7 on 2023-04-17 01:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0004_rename_producttypeattributes_producttypeattribute"),
    ]

    operations = [
        migrations.AddField(
            model_name="productinventory",
            name="is_digital",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="productinventory",
            name="is_on_sale",
            field=models.BooleanField(default=False),
        ),
    ]
