from django.utils.html import mark_safe
from unfold.admin import ModelAdmin
from django.contrib import admin

from .models import (
    Course, CourseRoadMap, CourseRoadMapField,
    Banner, HomeStats, SocialMediaLink, Teacher, About,
    ContactUs, Branch, Subject, Quiz, Certificate
)

# ========== IMAGE PREVIEW ==========

def image_preview(obj):
    if getattr(obj, "image", None):
        return mark_safe(f"<img src='{obj.image.url}' width='60' style='border-radius:8px;'>")
    return "-"
image_preview.short_description = "Rasm"


# ========== INLINE CLASSLAR ==========

class CourseRoadMapFieldInline(admin.TabularInline):
    model = CourseRoadMapField
    extra = 1


class CourseRoadMapInline(admin.TabularInline):
    model = CourseRoadMap
    extra = 1


# ========== COURSE ADMIN ==========

@admin.register(Course)
class CourseAdmin(ModelAdmin):
    list_display = ("id", image_preview, "name", "duration", "created_at")
    search_fields = ("name",)
    list_filter = ("duration",)
    readonly_fields = ("created_at", "updated_at")
    inlines = [CourseRoadMapInline]
    ordering = ("-created_at",)

    fieldsets = (
        ("Kurs maʼlumotlari", {
            "fields": ("image", "name", "description", "duration"),
        }),
        ("Texnik", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",)
        }),
    )


# ========== ROADMAP ADMIN ==========

@admin.register(CourseRoadMap)
class CourseRoadMapAdmin(ModelAdmin):
    list_display = ("id", "name", "course", "created_at")
    search_fields = ("name",)
    list_filter = ("course",)
    readonly_fields = ("created_at", "updated_at")
    inlines = [CourseRoadMapFieldInline]
    ordering = ("-created_at",)

    fieldsets = (
        ("Yo‘l xaritasi", {
            "fields": ("name", "course"),
        }),
        ("Texnik", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",)
        }),
    )


# ========== ROADMAP FIELD ADMIN ==========

@admin.register(CourseRoadMapField)
class CourseRoadMapFieldAdmin(ModelAdmin):
    list_display = ("id", "info", "road_maop", "created_at")
    search_fields = ("info",)
    list_filter = ("road_maop",)
    readonly_fields = ("created_at", "updated_at")
    ordering = ("-created_at",)

    fieldsets = (
        ("Matn", {
            "fields": ("info", "road_maop")
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


@admin.register(Subject)
class SubjectAdmin(ModelAdmin):
    list_display = ("name", image_preview, "created_at")
    search_fields = ("name",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(Quiz)
class QuizAdmin(ModelAdmin):
    list_display = ("name", "subject", "correct_answer", "created_at")
    search_fields = ("name",)
    list_filter = ("subject",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(Certificate)
class CertificateAdmin(ModelAdmin):
    list_display = ("full_name", image_preview, "level", "subject", "created_at")
    search_fields = ("full_name", "level")
    list_filter = ("subject",)
    readonly_fields = ("created_at", "updated_at")
