from django.shortcuts import render
from django_filters import rest_framework as filters
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import mixins
# from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from ecommerce.inventory.models import Product, ProductInventory

from .serializers import ProductInventorySerializer, ProductSerializer

# Create your views here.
product_tag = extend_schema(tags=["Products"])
product_inventory_tag = extend_schema(tags=["Product Inventory"])


# ----------------------------------------------------------
@extend_schema_view(
    list=product_tag,
    retrieve=product_tag,
    # update=product_tag,
    # partial_update=product_tag,
    create=product_tag,
    # destroy=product_tag,
)
class ProductView(
    GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = "slug"
    filterset_fields = ("category",)
    search_fields = ("name",)
    ordering_fields = [
        "name",
    ]

    def retrieve(self, request, *args, **kwargs):
        self.queryset = Product.objects.filter(category__slug=kwargs["slug"])
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)
        return super().retrieve(request, *args, **kwargs)


# ----------------------------------------------------------
@extend_schema_view(list=product_inventory_tag, retrieve=product_inventory_tag)
class ProductInventoryView(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer
    lookup_field = "slug"

    # ------------------------------
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    # ------------------------------
    def retrieve(self, request, *args, **kwargs):
        self.queryset = ProductInventory.objects.filter(
            product__category__slug=kwargs["slug"]
        ).filter(is_default=True)

        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)
