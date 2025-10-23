# banners/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'image_preview')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)

    def image_preview(self, obj):
        """
        Rasmni HTML <img> orqali xavfsiz ko'rsatadi.
        format_html avtomatik escaping qilgach, string interpolation xavfsiz bo'ladi.
        """
        if obj.image:
            return format_html(
                '<img src="{}" width="120" style="object-fit: cover; border-radius: 8px;" />',
                obj.image.url
            )
        return "—"
    image_preview.short_description = "Banner rasmi"
    image_preview.admin_order_field = 'image'  # optional: ruyxatni sortlashda yordam beradi
