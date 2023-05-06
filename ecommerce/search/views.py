from django.http import HttpResponse
from drf_spectacular.utils import extend_schema, extend_schema_view
from elasticsearch_dsl import Q
from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.mixins import ListModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from ..DRF.serializers import ProductInventorySerializer
from .documents import ProductInventoryDocument


# ---------------------------------------------------------------
@extend_schema_view(
    get=extend_schema(
        tags=["Search"], description="Search The Database using Product name and Brand Name"
    )
)
class SearchProductInventory(APIView, PageNumberPagination):
    serializer_class = ProductInventorySerializer
    search_document = ProductInventoryDocument
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        # We implement The Try Except Model To make Sure The Elastic Search Works as expected

        # query = request.query_params.get("query")
        # if not query:
        #     return Response(
        #         {"message": "The Search Query Was Not Found"},
        #         status=status.HTTP_417_EXPECTATION_FAILED,
        #     )

        try:
            # get the multimatch query

            q = Q(
                "multi_match",
                query=kwargs["query"],
                fields=["product.name", "brand.name"],
            )
            # search in the elastic search DataBase
            search = self.search_document.search().query(q)
            # excute The Search
            response = search.execute()
            # paginate
            results = self.paginate_queryset(response, request=request)
            if results:
                serializer = self.serializer_class(results, many=True)
                return self.get_paginated_response(serializer.data)

        except Exception as e:
            return HttpResponse(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
