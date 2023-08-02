from django.contrib import admin
from .models import Company, Category, Product, ProductRating, CompanyProduct
from parler.admin import TranslatableAdmin


@admin.register(ProductRating)
class ProductRatingAdmin(admin.ModelAdmin):
    list_display = ['product', 'rating_stars', 'name', 'email']
    list_filter = ['rating_stars']
    search_fields = ['product__name', 'name', 'email']

@admin.register(CompanyProduct)
class CompanyProductAdmin(admin.ModelAdmin):
    list_display = ['company', 'product']
    search_fields = ['company__name', 'product__name']


class CategoryAdmin(TranslatableAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']
    list_per_page = 20
    fieldsets = (
        (None, {
            'fields': ('name',),
        }),
    )


class ProductAdmin(TranslatableAdmin):
    list_display = ['name', 'created_at', 'is_featured', 'views']
    list_display_links = ['name']
    search_fields = ['name', 'compound', 'tag']
    list_per_page = 20
    list_filter = ['is_featured', 'category']
    list_editable = ['is_featured']

    fieldsets = (
        (None, {
            'fields': ('name', 'compound', 'tag', 'category', 'image', 'is_featured', 'created_at', 'updated_at', 'views', 'slug'),
        },),
    )
    readonly_fields = ['views', 'slug']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
