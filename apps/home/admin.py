from django.contrib import admin
from parler.admin import TranslatableAdmin
from django.utils.html import format_html
from .models import Position
# Register your models here.


class PositionAdmin(TranslatableAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']
    list_per_page = 20
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
    )

admin.site.register(Position, PositionAdmin)