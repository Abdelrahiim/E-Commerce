from rest_framework import serializers

from ecommerce.inventory.models import (
    Brand,
    Media,
    Product,
    ProductAttributeValue,
    ProductInventory,
    ProductType,
    Stock,
)


# ---------------------------------------------------------------
class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ["name"]


# ---------------------------------------------------------------
class ProductAttributeValueSerializer(serializers.ModelSerializer):
    # ------------------------------
    class Meta:
        model = ProductAttributeValue
        exclude = ["id"]
        depth = 1


# ---------------------------------------------------------------
class MediaSerializer(serializers.ModelSerializer):
    # ------------------------------
    class Meta:
        model = Media
        fields = ["image", "alt_text"]


# ---------------------------------------------------------------
class BrandSerializer(serializers.ModelSerializer):
    # -----------------------------
    class Meta:
        model = Brand
        fields = ("name",)


# ---------------------------------------------------------------
class ProductSerializer(serializers.ModelSerializer):
    # -----------------=============
    class Meta:
        model = Product
        fields = ["name"]
        read_only = True
        editable = False


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ["units"]
        read_only = True
        editable = False


# ---------------------------------------------------------------
class ProductInventorySerializer(serializers.ModelSerializer):
    # brand = BrandSerializer(many=False, read_only=True)
    # # for many to many relationship Like in This Case We Need to use source
    # product_attributes = ProductAttributeValueSerializer(many=True, source="attribute_values")
    # image = MediaSerializer(source="media_product_inventory", many=True)
    # price = serializers.DecimalField(source="retail_price", max_digits=5, decimal_places=2)
    # type = ProductTypeSerializer(many=True, read_only=True)

    product = ProductSerializer(many=False, read_only=True)
    stock = StockSerializer(
        source="Stock_Product_inventory"
    )  # The Source == related_name in The Model
    brand = BrandSerializer(read_only=True)

    # ------------------------------
    class Meta:
        model = ProductInventory
        fields = ["id", "sku", "store_price", "is_default", "product", "stock", "brand"]
        # exclude = ["id", "created_at", "updated_at"]
        readonly = True
        editable = False
