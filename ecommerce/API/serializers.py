from rest_framework import serializers

from ecommerce.inventory.models import (
    Brand,
    Category,
    Media,
    Product,
    ProductAttributeValue,
    ProductInventory,
)


# ---------------------------------------------------------------
class CategorySerializer(serializers.ModelSerializer):
    # ------------------------------
    class Meta:
        model = Category
        fields = ["name", "slug", "is_active"]
        read_only = True


# ---------------------------------------------------------------
class ProductSerializer(serializers.ModelSerializer):
    # ------------------------------
    class Meta:
        model = Product
        fields = ["name", "web_id"]
        read_only = True
        editable = False


# ---------------------------------------------------------------
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name"]
        read_only = True


# ---------------------------------------------------------------
class ProductAttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeValue
        depth = 2
        exclude = ["id"]
        read_only = True


# ---------------------------------------------------------------
class ProductMediaSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Media
        fields = ["image", "alt_text"]
        read_only = True
        editable = False

    def get_image(self, obj):
        return obj.image.url


# ---------------------------------------------------------------
class ProductInventorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)
    # any ForeignKey We Need To Add The Source or it will Not Work
    media = ProductMediaSerializer(source="media_product_inventory", many=True, read_only=True)

    brand = BrandSerializer(many=False, read_only=True)
    attributes = ProductAttributeValueSerializer(
        source="attribute_values", many=True, read_only=True
    )

    class Meta:
        model = ProductInventory
        fields = [
            "id",
            "sku",
            "store_price",
            "is_default",
            "brand",
            "product",
            "weight",
            "media",
            "attributes",
            "product_type",
        ]
        read_only = True
