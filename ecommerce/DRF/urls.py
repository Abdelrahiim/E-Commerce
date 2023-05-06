from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProductInventoryView, ProductView

router = DefaultRouter()

router.register(
    "products",
    viewset=ProductView,
    basename="All Products",
)
router.register(r"product-inventory", viewset=ProductInventoryView, basename="All Products")

# ---------------------------------------------------------------
urlpatterns = [
    path("", include(router.urls), name="Products"),
]
