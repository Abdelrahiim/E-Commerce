"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

# from drf_yasg import openapi
# from drf_yasg.views import get_schema_view
# from rest_framework import permissions

# ---------------------------------------------------------------
# Schema View
# schema_view = get_schema_view(
#     openapi.Info(
#         title="E-Commerce API",
#         default_version="v1.2",
#         description="Test description",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="contact@snippets.local"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=[permissions.AllowAny],
# )

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),  # For Debugging Toolbar
    path("demo/", include("ecommerce.demo.urls")),
    # path("api/", include("ecommerce.DRF.urls")),
    path("search/", include("ecommerce.search.urls")),
    path("api/", include("ecommerce.API.urls")),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    # re_path(
    #     r"^swagger(?P<format>\.json|\.yaml)$",
    #     schema_view.without_ui(cache_timeout=0),
    #     name="schema-json",
    # ),
    # # For Documentation With Swaggeer
    # path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    # # For Documentation With redoc
    # path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
