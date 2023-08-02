from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class Company(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=255, verbose_name=_('Name')),
        description=models.TextField(blank=False, null=False, verbose_name=_('Description'))
    )
    type_product = models.CharField(max_length=100)
    count_product = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=20)
    found_date = models.DateField()
    rating_stars = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    telegram = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')
        ordering = ["-rating_stars", "translations__name"]

    def __str__(self):
        return self.name


class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=255, verbose_name=_('Name')),
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Product(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=300, verbose_name=_('Nomi')),
        compound = models.CharField(max_length=1000, verbose_name=_('maxsulot haqida')),
        tag = models.TextField(verbose_name=_('Maqola')),
    )
    category = models.ForeignKey(Category,on_delete=models.CASCADE,  verbose_name=_('Kategorylari'))
    image = models.ImageField(upload_to='post_images', verbose_name=_('Rasm'))
    created_at = models.DateTimeField(verbose_name=_('Created at'))
    updated_at = models.DateTimeField(verbose_name=_('Updated at'))
    is_featured = models.BooleanField(default=False, verbose_name=_('Maxus post'))
    slug = models.SlugField(max_length=255, verbose_name=_('Slug'))
    views = models.IntegerField(default=0, verbose_name=_('Ko\'rilganlar soni'))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('MAXSULOT')
        verbose_name_plural = _('Mahsulotlar')
        ordering = ['-created_at']


class ProductRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    rating_stars = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    comment = models.TextField()
    name = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        verbose_name = _('Product Rating')
        verbose_name_plural = _('Product Ratings')
        ordering = ["-rating_stars"]

    def __str__(self):
        return f"{self.product.name} - {self.rating_stars} stars"


class CompanyProduct(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='company_products')

    class Meta:
        verbose_name = _('Company Product')
        verbose_name_plural = _('Company Products')
        unique_together = [['company', 'product']]  # Ensures that a company-product pair is unique

    def __str__(self):
        return f"{self.company.name} - {self.product.name}"
