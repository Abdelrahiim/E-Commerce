from typing import Any

from django.contrib import admin

from .models import Coupon, ProductOnPromotion, Promotion, PromoType
from .tasks import promotion_management, promotion_prices


# Register your models here.
class ProductOnPromotionAdmin(admin.StackedInline):
    model = Promotion.product_on_promotion.through
    extra = 4
    raw_id_fields = ("product_inventory_id",)


class ProductInventoryList(admin.ModelAdmin):
    model = Promotion
    inlines = (ProductOnPromotionAdmin,)
    list_display = ("name", "is_active", "promo_start", "promo_end")

    def save_model(self, request, obj, form, change) -> None:
        super().save_model(request, obj, form, change)
        promotion_prices.delay(obj.promo_reduction, obj.id)
        promotion_management.delay()


admin.site.register(Promotion, ProductInventoryList)
admin.site.register(PromoType)
admin.site.register(Coupon)
