from django.contrib import admin
from .models import Company, Category, Product, ProductRating, CompanyProduct, SubCategory
from parler.admin import TranslatableAdmin

@admin.register(ProductRating)
class ProductRatingAdmin(admin.ModelAdmin):
    list_display = ['product', 'star', 'review_date', 'email']
    list_filter = ['star']
    search_fields = ['product__name', 'email']
    list_per_page = 20

    fieldsets = (
        (None, {
            'fields': ('product', 'star', 'review_comment', 'review_date', 'email'),
        }),
    )
    readonly_fields = ['review_date']

@admin.register(CompanyProduct)
class CompanyProductAdmin(admin.ModelAdmin):
    list_display = ['company', 'product']
    search_fields = ['company__name', 'product__name']


class CategoryAdmin(TranslatableAdmin):
    list_display = ['name']
    list_display_links = ['name',]
    search_fields = ['name']
    list_per_page = 20
    fieldsets = (
        (None, {
            'fields': ('name', 'image'),
        }),
    )

admin.site.register(Category, CategoryAdmin)




class ProductAdmin(TranslatableAdmin):
    list_display = ['name', 'created_at', 'is_featured', 'views', 'campany']
    list_display_links = ['name']
    search_fields = ['name', 'compound', 'tag']
    list_per_page = 20
    list_filter = ['is_featured', 'category']
    list_editable = ['is_featured']

    fieldsets = (
        (None, {
            'fields': ('name', 'compound', 'tag', 'campany', 'category', 'image', 'is_featured', 'created_at', 'updated_at', 'views'),
        },),
    )
    readonly_fields = ['views']


admin.site.register(Product, ProductAdmin)

from django.utils.html import format_html


class CompanyAdmin(TranslatableAdmin):
    list_display = ['name', 'type_product', 'created_at']
    list_display_links = ['name']
    search_fields = ['name', 'type_product__name']
    list_per_page = 20

    def view_location_button(self, obj):
        return format_html('<a href="https://maps.google.com/?q={}" target="_blank">View Location</a>', obj.location)
    
    view_location_button.short_description = 'View Location'

    list_display = ['name', 'type_product', 'created_at', 'view_location_button']
    
    fieldsets = (
        (None, {
            'fields': ('name', 'type_product', 'image', 'phone_number','description','location')
        }),
        ('Social Media Links', {
            'fields': ('facebook', 'instagram', 'telegram', 'youtube'),
            'classes': ('collapse',),
        }),
    )
    
    readonly_fields = ['created_at']




class SubCategoryAdmin(TranslatableAdmin):
    list_display = ['name', 'category', 'is_active']
    list_display_links = ['name']
    search_fields = ['name', 'category__name']
    list_filter = ['category', 'is_active']
    list_per_page = 20

    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'is_active'),
        }),
    )

admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Company, CompanyAdmin)


# class TypeProductAdmin(TranslatableAdmin):
#     list_display = ['name', 'is_active']
#     list_display_links = ['name']
#     search_fields = ['translations__name']  # Search by translated name
#     list_per_page = 20
#     list_filter = ['is_active']

#     fieldsets = (
#         (None, {
#             'fields': ('name', 'is_active'),
#         }),
#     )

# admin.site.register(TypeProduct, TypeProductAdmin)
























