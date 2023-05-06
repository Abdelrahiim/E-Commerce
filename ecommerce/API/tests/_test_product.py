import json

import pytest

from .utils import ConvertToDotNotation


# ---------------------------------------------------------------
def test_get_product_by_category(api_client, single_product):
    product = single_product
    category = product.category.values("slug")[0]["slug"]
    endpoint = f"/api/inventory/product/category/{category}"
    response = api_client().get(endpoint)
    expected_json = [
        {
            "name": product.name,
            "web_id": product.web_id,
        }
    ]
    assert response.status_code == 200
    assert response.data == expected_json


# ---------------------------------------------------------------
def test_get_product_inventory_by_web_id(api_client, single_sub_product_with_media_and_attributes):
    fixture = ConvertToDotNotation(single_sub_product_with_media_and_attributes)
    endpoint = f"/api/inventory/{fixture.inventory.product.web_id}"
    print("endpoint", endpoint)
    response = api_client().get(endpoint)
    print("response", response.content)
    expected_json = [
        {
            "id": fixture.inventory.id,
            "sku": fixture.inventory.sku,
            "store_price": fixture.inventory.store_price,
            "is_default": fixture.inventory.is_default,
            "brand": {"name": fixture.inventory.brand.name},
            "product": {
                "name": fixture.inventory.product.name,
                "web_id": fixture.inventory.product.web_id,
            },
            "is_on_sale": fixture.inventory.is_on_sale,
            "weight": fixture.inventory.weight,
            "media": [
                {
                    "image": fixture.media.image.url,
                    "alt_text": fixture.media.alt_text,
                }
            ],
            "attributes": [
                {
                    "attribute_value": fixture.attribute.attribute_value,
                    "product_attribute": {
                        "id": fixture.attribute.id,
                        "name": fixture.attribute.product_attribute.name,
                        "description": fixture.attribute.product_attribute.description,
                    },
                }
            ],
            "product_type": fixture.inventory.product_type.id,
        }
    ]
    print("excepted", expected_json)
    assert response.status_code == 200
    assert json.loads(response.content) == expected_json
