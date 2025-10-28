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
from django import forms
from django.utils.html import mark_safe


# ========== IMAGE PREVIEW ==========

def image_preview(obj):
    if getattr(obj, "image", None):
        return mark_safe(f"<img src='{obj.image.url}' width='60' style='border-radius:8px;'/>")
    return "-"
image_preview.short_description = "Rasm"


# ---------- Qo'shma style (aniq ko'rinishi uchun) ----------
INPUT_STYLE = {
    "style": (
        "border:1px solid #6b7280;"
        "background:#0b1220;"
        "color:#ffffff;"
        "padding:8px 10px;"
        "border-radius:8px;"
        "width:100%;"
        "box-sizing:border-box;"
    )
}

TEXTAREA_STYLE = {
    "style": (
        "border:1px solid #6b7280;"
        "background:#0b1220;"
        "color:#ffffff;"
        "padding:10px 12px;"
        "border-radius:8px;"
        "width:100%;"
        "box-sizing:border-box;"
    )
}


# ---------- Formlar (aniq label/placeholder + ko'rinadigan style) ----------
class CourseRoadMapForm(forms.ModelForm):
    class Meta:
        model = CourseRoadMap
        fields = ("name",)
        labels = {"name": "Yo‘l xaritasi nomi"}
        help_texts = {"name": "Masalan: Backend asoslari"}
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "Masalan: Backend asoslari", **INPUT_STYLE}
            )
        }


class CourseRoadMapFieldForm(forms.ModelForm):
    class Meta:
        model = CourseRoadMapField
        fields = ("info",)
        labels = {"info": "Tavsif (bosqich mazmuni)"}
        help_texts = {"info": "Qisqacha mazmun: nimalar o‘rganiladi?"}
        widgets = {
            "info": forms.Textarea(
                attrs={"rows": 4, "placeholder": "Masalan: Python sintaksisi, o‘zgaruvchilar, if/for...", **TEXTAREA_STYLE}
            )
        }


# ---------- Nested inlines (collapse yo'q — hammasi ochiq) ----------
class CourseRoadMapFieldInline(nested_admin.NestedStackedInline):
    model = CourseRoadMapField
    form = CourseRoadMapFieldForm
    extra = 0
    can_delete = True
    verbose_name = "Yo‘l xaritasi matni"
    verbose_name_plural = "Yo‘l xaritasi matnlari"
    fieldsets = (
        ("Yo‘l xaritasi matnlari", {
            "description": "Bu bo‘limda shu yo‘l xaritasining ichki bosqichlarini tavsiflab yozing.",
            "fields": ("info",),
        }),
    )


class CourseRoadMapInline(nested_admin.NestedStackedInline):
    model = CourseRoadMap
    form = CourseRoadMapForm
    extra = 0
    inlines = [CourseRoadMapFieldInline]
    verbose_name = "Yo‘l xaritasi"
    verbose_name_plural = "Yo‘l xaritalari"
    fieldsets = (
        ("Yo‘l xaritasi", {
            "description": "Har bir yo‘l xaritasiga nom bering (masalan, ‘Backend asoslari’). Pastda uning bosqichlarini to‘ldirasiz.",
            "fields": ("name",),
        }),
    )


# ---------- Course admin ----------
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
            # collapse olib tashladik — ko‘rinishi aniq bo‘lsin desangiz qoldiramiz
            # "classes": ("collapse",)
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
