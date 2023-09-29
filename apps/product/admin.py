from django.contrib import admin
from .models import Company, Category, Product, ProductRating, SubCategory, ProductImage , Application, Question 
from parler.admin import TranslatableAdmin
from django.utils.html import format_html


@admin.register(ProductRating)
class ProductRatingAdmin(admin.ModelAdmin):
    list_display = ['name','product', 'star', 'review_date', 'email']
    list_filter = ['star']
    search_fields = ['product__name', 'email']
    list_per_page = 20

    fieldsets = (
        (None, {
            'fields': ('name','product', 'star', 'review_comment', 'review_date', 'email'),
        }),
    )
    readonly_fields = ['review_date']


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



class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(TranslatableAdmin):
    inlines = [ProductImageInline]
    list_display = ['name', 'created_at',  'company', 'short_description', 'is_featured']
    list_display_links = ['name']
    search_fields = ['name',  'tag']
    list_per_page = 20
    list_filter = [ 'category', 'mode_in']

    fieldsets = (
        (None, {
            'fields': ('name','mode_in','description', 'tag', 'company', 'category',  'created_at', 'is_featured', 'updated_at', 'short_description'),
        },),
    )

admin.site.register(Product, ProductAdmin)

class CompanyAdmin(TranslatableAdmin):
    list_display = ['name', 'type_product', 'country', 'short_description', 'created_at', 'view_location_button']
    list_display_links = ['name']
    search_fields = ['name', 'type_product__name']
    list_per_page = 20

    def view_location_button(self, obj):
        return format_html('<a href="https://maps.google.com/?q={}" target="_blank">View Location</a>', obj.location)
    
    view_location_button.short_description = 'View Location'

    fieldsets = (
        (None, {
            'fields': ('name', 'type_product', 'image', 'country', 'phone_number', 'description', 'short_description', 'location', 'workers_amount')
        }),
         ('Key Company info', {
            'fields': ('type_position', 'found_year'),
            'classes': ('collapse',),
        }),
        ('Social Media Links', {
            'fields': ('facebook', 'instagram', 'telegram', 'youtube'),
            'classes': ('collapse',),
        }),
    )
    
    readonly_fields = ['created_at']

admin.site.register(Company, CompanyAdmin)


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


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'display_checked', 'date', 'tarif']
    list_filter = ['checked']
    search_fields = ['name', 'phone_number']
    list_per_page = 50
    readonly_fields = ['date']

    def display_checked(self, obj):
        if obj.checked:
            return format_html('<span style="color: green;"><b>&#10004;</b></span>')  # Checked icon
        else:
            return format_html('<span style="color: red;"><b>&#10008;</b></span>')  # X icon

    display_checked.short_description = 'Checked'


admin.site.register(Application, ApplicationAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'display_checked', 'date']
    list_filter = ['checked']
    search_fields = ['name', 'phone_number', 'campany_name']
    list_per_page = 50
    readonly_fields = ['date']

    def display_checked(self, obj):
        if obj.checked:
            return format_html('<span style="color: green;"><b>&#10004;</b></span>')  # Checked icon
        else:
            return format_html('<span style="color: red;"><b>&#10008;</b></span>')  # X icon

    display_checked.short_description = 'Checked'


admin.site.register(Question, QuestionAdmin)
























