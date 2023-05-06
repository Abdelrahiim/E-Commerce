from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("cat/", views.CategoryView.as_view(), name="categories"),
    path(
        "product-by-category/<slug:category>",
        views.ProductByCategory.as_view(),
        name="product_by_category",
    ),
    path(
        "product-detail/<slug:slug>",
        views.ProductDetail.as_view(),
        name="product_detail",
    ),
]
