from decimal import Decimal

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from ecommerce.inventory.models import ProductInventory


# Create your models here.
# ---------------------------------------------------------------
class PromoType(models.Model):
    name = models.CharField(max_length=120)

    # ------------------------------
    def __str__(self) -> str:
        return self.name


# ---------------------------------------------------------------
class Coupon(models.Model):
    name = models.CharField(max_length=120)
    coupon_code = models.CharField(max_length=23)


# ---------------------------------------------------------------
class Promotion(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True)
    promo_reduction = models.IntegerField()
    is_active = models.BooleanField(default=False)
    is_schedule = models.BooleanField(default=False)
    promo_start = models.DateField()
    promo_end = models.DateField()
    product_on_promotion = models.ManyToManyField(
        ProductInventory, related_name="products_on_promotion", through="ProductOnPromotion"
    )
    promo_type = models.ForeignKey(PromoType, related_name="promo_type", on_delete=models.PROTECT)
    coupon = models.ForeignKey(Coupon, related_name="coupon", on_delete=models.PROTECT)

    # ------------------------------
    def clean(self):
        if self.promo_start > self.promo_end:
            raise ValidationError(_("End Date Before Start Date"))

    # ------------------------------
    def __str__(self) -> str:
        return self.name


# ---------------------------------------------------------------
class ProductOnPromotion(models.Model):
    product_inventory_id = models.ForeignKey(
        ProductInventory, related_name="product_inventory", on_delete=models.PROTECT
    )
    promotion_id = models.ForeignKey(Promotion, related_name="Promotion", on_delete=models.CASCADE)
    promo_price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        default=Decimal("0.00"),
        validators=[MinValueValidator(Decimal("0.00"))],
    )
    price_override = models.BooleanField(default=False)

    # ------------------------------
    class Meta:
        unique_together = ("product_inventory_id", "promotion_id")
