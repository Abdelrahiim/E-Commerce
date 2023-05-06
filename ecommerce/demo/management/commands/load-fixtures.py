from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        call_command("makemigrations")
        call_command("migrate")
        call_command(
            "loaddata", "db_admin_fixture.json"
        )  # load The Admin Data To The Actual DataBase
        call_command(
            "loaddata", "db_category_fixture.json"
        )  # load The Category Data To The Actual DataBase
        call_command(
            "loaddata", "db_product_fixture.json"
        )  # load The Product Data To The Actual DataBase
        call_command("loaddata", "db_category_product_fixture.json")
        call_command(
            "loaddata", "db_brand_fixture.json"
        )  # load The brand Data To The Actual DataBase
        call_command(
            "loaddata", "db_type_fixture.json"
        )  # load The Product type Data To The Actual DataBase
        call_command(
            "loaddata", "db_product_inventory_fixture.json"
        )  # load The Product Inventory Data To The Actual DataBase
        call_command("loaddata", "db_media_fixture.json")
        call_command("loaddata", "db_stock_fixture.json")
        call_command("loaddata", "db_product_attribute_fixture.json")
        call_command("loaddata", "db_product_attribute_value_fixture.json")
        call_command("loaddata", "db_product_attribute_values_fixture.json")
        call_command("loaddata", "db_product_type_attributes_fixture.json")
