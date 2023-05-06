from django.urls import include, path, re_path

from .views import CategoryList, ProductByCategory, ProductInventoryByWebId

urlpatterns = [
    path("inventory/category/all/", CategoryList.as_view()),
    path("inventory/product/category/<str:query>", ProductByCategory.as_view()),
    path("inventory/<str:query>", ProductInventoryByWebId.as_view()),
]
