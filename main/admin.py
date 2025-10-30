from django.utils.html import mark_safe
from unfold.admin import ModelAdmin
from django.contrib import admin

from .models import (
    Course, CourseRoadMap, CourseRoadMapField,
    Banner, HomeStats, SocialMediaLink, Teacher, About,
    ContactUs, Branch, Subject, Quiz, Certificate, RegisterImage, TelegramAdmin, TestModel
)
from django.contrib.auth.models import Group
admin.site.unregister(Group)
from unfold.admin import ModelAdmin
from django.contrib import admin
import nested_admin
from .models import Course, CourseRoadMap, CourseRoadMapField
from django.utils.html import mark_safe

# Inlines for nested administration


class CourseRoadMapFieldInline(admin.TabularInline):
    model = CourseRoadMapField
    extra = 1
    fields = ('info_uz', 'info_ru', 'info_en')  # Show multilingual fields


class CourseRoadMapInline(admin.TabularInline):
    model = CourseRoadMap
    extra = 1
    inlines = [CourseRoadMapFieldInline]
    fields = ('name_uz', 'name_ru', 'name_en')  # Show multilingual fields


class QuizInline(admin.TabularInline):
    model = Quiz
    extra = 1
    fields = (
        'name_uz', 'name_ru', 'name_en',
        'answer1_uz', 'answer1_ru', 'answer1_en',
        'answer2_uz', 'answer2_ru', 'answer2_en',
        'answer3_uz', 'answer3_ru', 'answer3_en',
        'answer4_uz', 'answer4_ru', 'answer4_en',
        'correct_answer', 'difficulty'
    )


class CertificateInline(admin.TabularInline):
    model = Certificate
    extra = 1
    fields = ('full_name_uz', 'full_name_ru', 'full_name_en', 'level', 'image')


# ModelAdmins


@admin.register(Banner)
class BannerAdmin(ModelAdmin):
    list_display = ('title_uz', 'created_at')
    fields = (
        'title_uz', 'title_ru', 'title_en',
        'description_uz', 'description_ru', 'description_en',
        'image'
    )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(HomeStats)
class HomeStatsAdmin(ModelAdmin):
    list_display = ('students', 'year_exp', 'employment', 'university_student', 'created_at')
    fields = ('students', 'year_exp', 'employment', 'university_student')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(SocialMediaLink)
class SocialMediaLinkAdmin(ModelAdmin):
    list_display = ('telegram', 'instagram', 'youtube', 'facebook', 'location_uz', 'created_at')
    fields = (
        'telegram', 'instagram', 'youtube', 'facebook',
        'location_uz', 'location_ru', 'location_en'
    )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Course)
class CourseAdmin(ModelAdmin):
    list_display = ('name_uz', 'duration', 'created_at')
    inlines = [CourseRoadMapInline]
    fields = (
        'image',
        'name_uz', 'name_ru', 'name_en',
        'description_uz', 'description_ru', 'description_en',
        'duration'
    )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(CourseRoadMap)
class CourseRoadMapAdmin(ModelAdmin):
    list_display = ('name_uz', 'course', 'created_at')
    inlines = [CourseRoadMapFieldInline]
    fields = ('course', 'name_uz', 'name_ru', 'name_en')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(CourseRoadMapField)
class CourseRoadMapFieldAdmin(ModelAdmin):
    list_display = ('road_map', 'info_uz', 'created_at')
    fields = ('road_map', 'info_uz', 'info_ru', 'info_en')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Teacher)
class TeacherAdmin(ModelAdmin):
    list_display = ('full_name_uz', 'subject_uz', 'created_at')
    fields = (
        'image',
        'full_name_uz', 'full_name_ru', 'full_name_en',
        'subject_uz', 'subject_ru', 'subject_en',
        'about_uz', 'about_ru', 'about_en',
        'instagram', 'telegram', 'facebook', 'video'
    )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(About)
class AboutAdmin(ModelAdmin):
    list_display = ('students', 'exp', 'teachers', 'graduates', 'created_at')
    fields = (
        'students', 'exp', 'teachers', 'graduates',
        'image', 'lat', 'lot'
    )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(ContactUs)
class ContactUsAdmin(ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    fields = ('name', 'email', 'message')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name', 'email')


@admin.register(Branch)
class BranchAdmin(ModelAdmin):
    list_display = ('name_uz', 'lat', 'lot', 'created_at')
    fields = (
        'name_uz', 'name_ru', 'name_en',
        'about_uz', 'about_ru', 'about_en',
        'image', 'lat', 'lot'
    )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Subject)
class SubjectAdmin(ModelAdmin):
    list_display = ('name_uz', 'created_at')
    inlines = [QuizInline, CertificateInline]
    fields = ('name_uz', 'name_ru', 'name_en', 'image')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Quiz)
class QuizAdmin(ModelAdmin):
    list_display = ('name_uz', 'subject', 'difficulty', 'correct_answer', 'created_at')
    fields = (
        'subject',
        'name_uz', 'name_ru', 'name_en',
        'answer1_uz', 'answer1_ru', 'answer1_en',
        'answer2_uz', 'answer2_ru', 'answer2_en',
        'answer3_uz', 'answer3_ru', 'answer3_en',
        'answer4_uz', 'answer4_ru', 'answer4_en',
        'correct_answer', 'difficulty'
    )
    readonly_fields = ('created_at', 'updated_at')
    list_filter = ('difficulty', 'subject')


@admin.register(Certificate)
class CertificateAdmin(ModelAdmin):
    list_display = ('full_name_uz', 'subject', 'level', 'created_at')
    fields = (
        'image',
        'full_name_uz', 'full_name_ru', 'full_name_en',
        'level', 'subject'
    )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(RegisterImage)
class RegisterImageAdmin(ModelAdmin):
    list_display = ('image', 'created_at')
    fields = ('image',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(TelegramAdmin)
class TelegramAdminAdmin(ModelAdmin):
    list_display = ('telegram_id', 'name', 'created_at')
    fields = ('telegram_id', 'name')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('telegram_id', 'name')


@admin.register(TestModel)
class TestModelAdmin(ModelAdmin):
    list_display = ('title_uz', 'name_uz')
    fields = (
        'title_uz', 'title_ru', 'title_en',
        'name_uz', 'name_ru', 'name_en',
        'info_uz', 'info_ru', 'info_en'
    )