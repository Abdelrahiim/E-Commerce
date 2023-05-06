from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Count
from django.shortcuts import render
from django.views.generic import TemplateView

from ecommerce.inventory import models


# ---------------------------------------------------------------
class HomeView(TemplateView):
    template_name = "index.html"


# ---------------------------------------------------------------
class CategoryView(TemplateView):
    template_name = "category.html"

    # ------------------------------
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = models.Category.objects.all()  # Return all object in the database

        context["categories"] = data
        return context


# ---------------------------------------------------------------
class ProductByCategory(TemplateView):
    template_name = "product_by_category.html"

    # ------------------------------
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = (
            models.Product.objects.filter(category__name=kwargs["category"])
            .filter(product__is_default=True)
            .values("id", "name", "slug", "product__store_price", "category__name")
        )
        context["data"] = data

        return context


# ---------------------------------------------------------------
class ProductDetail(TemplateView):
    template_name = "product_detail.html"
    filter_arguments = []
    context = dict()

    # ------------------------------
    def get(self, request, *args, **kwargs):
        print("there are values")
        for value in request.GET.values():
            self.filter_arguments.append(value)

        return super().get(request, *args, **kwargs)

    # ------------------------------
    def get_context_data(self, **kwargs):
        # -------------------
        if self.filter_arguments == []:
            data = (
                models.ProductInventory.objects.filter(product__slug=kwargs["slug"])
                .filter(is_default=True)
                .values(
                    "id",
                    "product__name",
                    "sku",
                    "store_price",
                    "Stock_Product_inventory__units",
                )
                .annotate(field_a=ArrayAgg("attribute_values__attribute_value"))
            )
            print(data)
        # -------------------
        else:
            data = (
                models.ProductInventory.objects.filter(product__slug=kwargs["slug"])
                # # .filter(is_default=True)
                .filter(attribute_values__attribute_value__in=self.filter_arguments)
                .annotate(num_tags=Count("attribute_values"))
                .filter(num_tags=len(self.filter_arguments))
                .values(
                    "id",
                    "product__name",
                    "sku",
                    "store_price",
                    "Stock_Product_inventory__units",
                )
                .annotate(field_a=ArrayAgg("attribute_values__attribute_value"))
            )

        y = (
            models.ProductInventory.objects.filter(product__slug=kwargs["slug"])
            .distinct()
            .values(
                "attribute_values__product_attribute__name",
                "attribute_values__attribute_value",
            )
        )

        z = (
            models.ProductTypeAttribute.objects.filter(
                product_type__product_type__product__slug=kwargs["slug"]
            )
            .distinct()
            .values("product_attribute__name")
        )
        print(data)
        self.filter_arguments.clear()
        self.context["data"] = data
        self.context["z"] = z
        self.context["y"] = y
        return self.context
