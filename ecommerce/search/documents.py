from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from ecommerce.inventory.models import Product, ProductInventory, Stock


# -----------------------------------------------------------------------------
@registry.register_document
class ProductInventoryDocument(Document):
    """
    Implementing Elastic Search on The Product Inventory
    """

    product = fields.ObjectField(
        properties={"name": fields.TextField(), "web_id": fields.TextField()}
    )
    # #  the Name is The related name
    Stock_Product_inventory = fields.NestedField(properties={"units": fields.IntegerField()})
    brand = fields.ObjectField(properties={"name": fields.TextField()})

    # ------------------------------
    class Index:
        name = "ProductInventory".lower()

    # ------------------------------
    class Django:
        model = ProductInventory
        # Match The Serializer
        fields = ["id", "sku", "store_price", "is_default"]
