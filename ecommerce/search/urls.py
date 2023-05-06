from django.urls import include, path

from .views import SearchProductInventory

urlpatterns = [
    path("<str:query>", view=SearchProductInventory.as_view()),
]
