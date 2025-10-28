from django.utils.html import mark_safe
from unfold.admin import ModelAdmin
from django.contrib import admin

from .models import (
    Course, CourseRoadMap, CourseRoadMapField,
    Banner, HomeStats, SocialMediaLink, Teacher, About,
    ContactUs, Branch, Subject, Quiz, Certificate
)
from django.contrib.auth.models import Group
admin.site.unregister(Group)
from unfold.admin import ModelAdmin
from django.contrib import admin
import nested_admin
from .models import Course, CourseRoadMap, CourseRoadMapField
from django.utils.html import mark_safe


# ========== IMAGE PREVIEW ==========

def image_preview(obj):
    if getattr(obj, "image", None):
        return mark_safe(f"<img src='{obj.image.url}' width='60' style='border-radius:8px;'/>")
    return "-"
image_preview.short_description = "Rasm"


# ========== INLINE CLASSLAR ==========

class CourseRoadMapFieldInline(nested_admin.NestedTabularInline):
    model = CourseRoadMapField
    extra = 1
    verbose_name = "Yo‘l xaritasi matni"
    verbose_name_plural = "Yo‘l xaritasi matnlari"


class CourseRoadMapInline(nested_admin.NestedTabularInline):
    model = CourseRoadMap
    extra = 1
    verbose_name = "Yo‘l xaritasi"
    verbose_name_plural = "Yo‘l xaritalari"
    inlines = [CourseRoadMapFieldInline]


# ========== COURSE ADMIN ==========

@admin.register(Course)
class CourseAdmin(nested_admin.NestedModelAdmin, ModelAdmin):
    list_display = ("id", image_preview, "name", "duration", "created_at")
    search_fields = ("name",)
    list_filter = ("duration",)
    readonly_fields = ("created_at", "updated_at")
    ordering = ("-created_at",)
    inlines = [CourseRoadMapInline]

    fieldsets = (
        ("Kurs maʼlumotlari", {
            "fields": ("image", "name", "description", "duration"),
        }),
        ("Texnik", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",)
        }),
    )


# ========== QOLGAN MODELLAR ==========

@admin.register(Banner)
class BannerAdmin(ModelAdmin):
    list_display = ("title", image_preview, "created_at")
    search_fields = ("title",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(HomeStats)
class HomeStatsAdmin(ModelAdmin):
    list_display = ("students", "year_exp", "employment", "university_student")
    readonly_fields = ("created_at", "updated_at")


@admin.register(SocialMediaLink)
class SocialMediaLinkAdmin(ModelAdmin):
    list_display = ("telegram", "instagram", "youtube", "facebook", "location")
    readonly_fields = ("created_at", "updated_at")


@admin.register(Teacher)
class TeacherAdmin(ModelAdmin):
    list_display = ("full_name", "subject", image_preview, "created_at")
    search_fields = ("full_name", "subject")
    readonly_fields = ("created_at", "updated_at")


@admin.register(About)
class AboutAdmin(ModelAdmin):
    list_display = ("students", "exp", "teachers", "graduates", image_preview)
    readonly_fields = ("created_at", "updated_at")


@admin.register(ContactUs)
class ContactUsAdmin(ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email")
    readonly_fields = ("created_at", "updated_at")


@admin.register(Branch)
class BranchAdmin(ModelAdmin):
    list_display = ("name", image_preview, "lat", "lot")
    search_fields = ("name",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(Quiz)
class QuizAdmin(ModelAdmin):
    list_display = ("name", "subject", "difficulty", "correct_answer", "created_at")
    search_fields = ("name",)
    list_filter = ("subject", "difficulty")
    readonly_fields = ("created_at", "updated_at")
    ordering = ("-created_at",)


@admin.register(Certificate)
class CertificateAdmin(ModelAdmin):
    list_display = ("full_name", image_preview, "level", "subject", "created_at")
    search_fields = ("full_name", "level")
    list_filter = ("subject",)
    readonly_fields = ("created_at", "updated_at")
