from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


# ---------------------------------------------------------------
class Category(MPTTModel):
    """
    Inventory Category Table With MPTT
    """

    name = models.CharField(
        max_length=100,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("category name"),
        help_text=_("format:required , max-100"),
    )
    slug = models.SlugField(
        max_length=150,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("category safe url"),
        help_text=_("format : required  letters,numbers,underscore or hyphens"),
    )
    is_active = models.BooleanField(default=True)
    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="children",
        blank=True,
        null=True,
        unique=False,
        verbose_name=_("parent of category"),
        help_text=_("format : not required"),
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("product_category")
        verbose_name_plural = "product_categories"  # To modify the admin page it will write product_categorys which is not right in English so We change it

    def __str__(self) -> str:
        return self.name


# ---------------------------------------------------------------
class Product(models.Model):
    """
    Inventory Product Table
    """

    web_id = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("product website Id"),
    )
    slug = models.SlugField(
        max_length=150,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Product Name safe url"),
    )

    name = models.CharField(
        max_length=150,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("Product name"),
    )
    description = models.TextField(
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("Product Description"),
    )
    category = TreeManyToManyField(Category)
    created_at = models.DateTimeField(
        auto_now_add=True,  #
        editable=False,
        verbose_name=_("date Product Created"),
    )
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    # ------------------------------
    def __str__(self) -> str:
        return f"{self.name} ==> {self.web_id}"


# ---------------------------------------------------------------
class ProductAttribute(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    # ------------------------------
    def __str__(self) -> str:
        return self.name


# ---------------------------------------------------------------
class ProductAttributeValue(models.Model):
    """
    Inventory Product Attribute Value
    """

    product_attribute = models.ForeignKey(ProductAttribute, on_delete=models.PROTECT)
    attribute_value = models.CharField(max_length=255)

    # ------------------------------
    def __str__(self) -> str:
        return f"{self.product_attribute.name} : {self.attribute_value}"


# ---------------------------------------------------------------
class ProductType(models.Model):
    """
    Inventory Product Type Table
    """

    name = models.CharField(max_length=255, unique=True, verbose_name=_("Product Type"))
    product_type_attributes = models.ManyToManyField(
        ProductAttribute, through="ProductTypeAttribute"
    )


# -----------------------------------------------------------------
class Brand(models.Model):
    """
    Inventory Brand Table
    """

    name = models.CharField(max_length=255, unique=True, verbose_name=_("Brand Name"))

    def __str__(self) -> str:
        return self.name


# ---------------------------------------------------------------
class ProductInventory(models.Model):
    """
    Inventory Product Inventory Table
    """

    sku = models.CharField(
        max_length=20,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("Stock Keeping Unit"),
    )
    upc = models.CharField(
        max_length=12,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("Universal Product Code"),
    )
    product_type = models.ForeignKey(
        ProductType, on_delete=models.PROTECT, related_name="product_type"
    )
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="product")
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="brand")

    attribute_values = models.ManyToManyField(
        ProductAttributeValue,
        related_name="product_attribute_values",
        through="ProductAttributeValues",
    )
    is_active = models.BooleanField(default=True)
    is_default = models.BooleanField(default=False)
    retail_price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        verbose_name=_("Recommended Retail Price"),
        validators=[MinValueValidator(Decimal(".01"))],
    )
    store_price = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name=_("Regular Store Price")
    )

    weight = models.FloatField(verbose_name=_("Product Weight"))

    is_digital = models.BooleanField(default=False)

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("date sub-product created"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("date sub-product updated"),
    )


class Media(models.Model):
    """
    Inventory Image Table
    """

    product_inventory = models.ForeignKey(
        ProductInventory,
        on_delete=models.PROTECT,
        related_name="media_product_inventory",
    )
    image = models.ImageField(
        unique=False,
        upload_to="images/",
        default="images/default.png",
        verbose_name=_("product image"),
    )
    alt_text = models.CharField(max_length=255, verbose_name=_("aleternative text"))
    is_feature = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# ---------------------------------------------------------------
class Stock(models.Model):
    """
    Inventory Stock Table
    """

    product_inventory = models.OneToOneField(
        ProductInventory,
        on_delete=models.PROTECT,
        related_name="Stock_Product_inventory",
    )
    last_checked = models.DateTimeField(null=True, blank=True)
    units = models.IntegerField(default=0)
    units_sold = models.IntegerField(default=0)


class ProductAttributeValues(models.Model):
    """
    Product attribute values link table
    """

    attributevalues = models.ForeignKey(
        ProductAttributeValue,
        related_name="attributevaluess",
        on_delete=models.PROTECT,
    )
    productinventory = models.ForeignKey(
        ProductInventory,
        related_name="productattributevaluess",
        on_delete=models.PROTECT,
    )

    class Meta:
        unique_together = (("attributevalues", "productinventory"),)


# -----------------------------------------------------------------
class ProductTypeAttribute(models.Model):
    product_attribute = models.ForeignKey(ProductAttribute, on_delete=models.PROTECT)
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT)

    class Meta:
        unique_together = (("product_attribute", "product_type"),)


# ------------------------------------------------------------------
