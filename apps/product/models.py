from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from parler.models import TranslatableModel, TranslatedFields
from tinymce.models import HTMLField
from .countries import Country
from apps.home.models import Position


class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=255, verbose_name=_('Name')),
    )
    image = models.ImageField(upload_to='category_images', verbose_name=_('Rasm'))
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    def subcategories(self):
        return SubCategory.objects.filter(category=self)
    

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')



class Company(TranslatableModel):
    translations = TranslatedFields(
        description=models.TextField(verbose_name=_('Description'), null=True, blank=True),
        short_description=models.TextField(verbose_name=_('Short Description'), null=True, blank=True, default="NEW"),
    )
    name = models.CharField(max_length=300, verbose_name=_('Nomi'))
    type_position = models.ForeignKey(
        Position ,  # Replace with your actual Category model
        on_delete=models.CASCADE,
        verbose_name=_('Biznes turi turi')
    )
    type_product = models.ForeignKey(
        Category,  # Replace with your actual Category model
        on_delete=models.CASCADE,
        verbose_name=_('Maxsulot turi')
    )
    location = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=2, choices=Country.choices)
    image = models.ImageField(upload_to='post_images', verbose_name=_('Rasm'))
    phone_number = PhoneNumberField(verbose_name=_('Phone number'))
    created_at = models.DateTimeField(auto_now_add=True)
    facebook = models.URLField(verbose_name=_('Facebook URL'), blank=True)
    instagram = models.URLField(verbose_name=_('Instagram URL'), blank=True)
    telegram = models.URLField(verbose_name=_('Telegram URL'), blank=True)
    youtube = models.URLField(verbose_name=_('YouTube URL'), blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Kampania')
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
        description = HTMLField(),
        tag = models.TextField(verbose_name=_('Tag')),
        short_description = models.TextField(verbose_name=_('short_description'), null=True , blank=True , default="NEW")

    )
    mode_in = models.CharField(
        max_length=2,
        choices=Country.choices,
        default=Country.UZBEKISTAN,
    )
    category = models.ForeignKey(SubCategory,on_delete=models.CASCADE,  verbose_name=_('Kategorylari'))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name=_('Created at'))
    is_featured = models.BooleanField(default=False) 
    updated_at = models.DateTimeField(verbose_name=_('Updated at'))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('MAXSULOT')
        verbose_name_plural = _('Mahsulotlar')
        ordering = ['-created_at']


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return f"Image for {self.product.name}"



class ProductRating(models.Model):
    name = models.CharField(max_length=123, help_text="Nomi")
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


class Application(models.Model):
    tarif = models.CharField(max_length=100, default="Рынок Узбекистана", null=True, blank=True, verbose_name="Tarif")
    name = models.CharField(max_length=123, help_text="Nomi", verbose_name="Name")
    location = models.CharField(max_length=255, help_text="Davlatlar", verbose_name="Location")
    phone_number = models.CharField(max_length=100, help_text="Telefon raqami", verbose_name="Phone Number")
    email = models.EmailField(max_length=254, null=True, blank=True, help_text="Email uchun", verbose_name="Email", unique=False)
    checked = models.BooleanField(default=False, help_text="Tekshirilganmi?", verbose_name="Checked")
    company_name = models.CharField(max_length=123, help_text="Kampaniya nomi", verbose_name="Company Name")
    date = models.DateTimeField(auto_now_add=True, help_text="Sana", verbose_name="Date")

    class Meta:
        verbose_name = _("Application")
        verbose_name_plural = _("Applications")

    def __str__(self):
        return self.name 
    
class Question(models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Product")
    name = models.CharField(max_length=123, help_text="Nomi", verbose_name="Name")
    location = models.CharField(max_length=255, default='Uzbekistan', help_text="Davlatlar", verbose_name="Location")
    phone_number = models.CharField(max_length=100, help_text="Telefon raqami", verbose_name="Phone Number")
    email = models.EmailField(max_length=254, null=True, blank=True, help_text="Email uchun", verbose_name="Email", unique=False)
    checked = models.BooleanField(default=False, help_text="Tekshirilganmi?", verbose_name="Checked")
    text = models.TextField(help_text="Matn", verbose_name="Text")
    date = models.DateTimeField(auto_now_add=True, help_text="Sana", verbose_name="Date")

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')

    def __str__(self):
        return self.name
    

