from django.shortcuts import render
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from ecommerce.inventory.models import Category, Product, ProductInventory

from .serializers import CategorySerializer, ProductInventorySerializer, ProductSerializer


# ---------------------------------------------------------------
@extend_schema_view(get=extend_schema(tags=["Categories"]))
class CategoryList(ListAPIView):
    # ------------------------------
    # @swagger_auto_schema(
    #     responses={200: CategorySerializer(many=True)},
    #     operation_description="GET api/inventory/category/all/",
    # )

    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        query = Category.objects.all()
        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data)


# ---------------------------------------------------------------
class ProductByCategory(ListAPIView):
    # ------------------------------
    # @swagger_auto_schema(
    #     responses={200: ProductSerializer(many=True)},
    #     operation_description="GET inventory/product/category/category_name",
    # )

    serializer_class = ProductSerializer

    @extend_schema(tags=["Products"])
    def get(self, request, *args, **kwargs):
        query = Product.objects.filter(category__slug=kwargs["query"])
        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data)


class ProductInventoryByWebId(APIView):
    """
    Return Product Inventory By Web_id
    """

    serializer_class = ProductInventorySerializer

    @extend_schema(tags=["Products"])
    def get(self, request, *args, **kwargs):
        queryset = ProductInventory.objects.filter(product__web_id=kwargs["query"])
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
