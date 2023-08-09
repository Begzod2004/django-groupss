from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from parler.models import TranslatableModel, TranslatedFields

# class TypeProduct(TranslatableModel):
#     translations = TranslatedFields(
#         name=models.CharField(max_length=255, verbose_name=_('Name')),
#     )
#     is_active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = _('Tur kategoryasi')
#         verbose_name_plural = _('Tur kategoryalari')

class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=255, verbose_name=_('Name')),
    )
    image = models.ImageField(upload_to='category_images', verbose_name=_('Rasm'))
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

class Company(TranslatableModel):
    translations = TranslatedFields(
        description = models.TextField(verbose_name=_('Qisqacha malumot'), help_text=_('Qisqacha malumot')),
    )
    name=models.CharField(max_length=300, verbose_name=_('Nomi'))
    type_product = models.ForeignKey(Category ,on_delete=models.CASCADE,  verbose_name=_('Maxsulot turi'))
    location = models.CharField(max_length=255,null=True, blank=True)
    image = models.ImageField(upload_to='post_images', verbose_name=_('Rasm'))
    phone_number = PhoneNumberField(verbose_name=_('Phone number'))
    created_at = models.DateTimeField(auto_now_add=True)
    facebook = models.URLField(verbose_name=_('Instagram URL'))
    instagram = models.URLField(verbose_name=_('Instagram URL'))
    telegram = models.URLField(verbose_name=_('Telegram URL'))
    youtube = models.URLField(verbose_name=_('Youtube URL'))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Kamapania')
        verbose_name_plural = _('Kampaniyalar')


class SubCategory(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=255, verbose_name=_('Name')),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Parent Category'))
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Subcategory')
        verbose_name_plural = _('Subcategories')


class Product(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=300, verbose_name=_('Nomi')),
        compound = models.CharField(max_length=1000, verbose_name=_('maxsulot haqida')),
        tag = models.TextField(verbose_name=_('Tag')),
    )
    category = models.ForeignKey(Category,on_delete=models.CASCADE,  verbose_name=_('Kategorylari'))
    campany = models.ForeignKey(Company, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images', verbose_name=_('Rasm'))
    created_at = models.DateTimeField(verbose_name=_('Created at'))
    updated_at = models.DateTimeField(verbose_name=_('Updated at'))
    is_featured = models.BooleanField(default=False, verbose_name=_('Maxus post'))
    views = models.IntegerField(default=0, verbose_name=_('Ko\'rilganlar soni'))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('MAXSULOT')
        verbose_name_plural = _('Mahsulotlar')
        ordering = ['-created_at']


class ProductRating(models.Model):
    star = models.IntegerField(default=0 , verbose_name = "star")
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='productreview')
    review_comment = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True, verbose_name='review_created_date')
    email = models.EmailField()

    class Meta:
        verbose_name = _('Product Rating')
        verbose_name_plural = _('Product Ratings')

    def __str__(self):
        return f"{self.product.name} - {self.star} stars"


class CompanyProduct(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='company_products')

    class Meta:
        verbose_name = _('Company Product')
        verbose_name_plural = _('Company Products')
        unique_together = [['company', 'product']]  # Ensures that a company-product pair is unique

    def __str__(self):
        return f"{self.company.name} - {self.product.name}"
