from rest_framework import serializers
from .models import (
    Banner, HomeStats, SocialMediaLink, CourseRoadMapField, CourseRoadMap,
    Course, Teacher, About, ContactUs, Branch, Subject, Quiz, Certificate, RegisterImage, TestModel
)

class BannerSerializer(serializers.ModelSerializer):
    translations = serializers.SerializerMethodField()
    class Meta:
        model = Banner
        fields = ['id', 'image', 'translations']

    def get_translations(self, obj):
        return {
            'uz': {
                'title': obj.title_uz,
                'description': obj.description_uz,
            },
            'ru': {
                'title': obj.title_ru,
                'description': obj.description_ru,
            },
            'en': {
                'title': obj.title_en,
                'description': obj.description_en,
            },
        }


class HomeStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeStats
        fields = "__all__"


class SocialMediaLinkSerializer(serializers.ModelSerializer):
    translations = serializers.SerializerMethodField()
    class Meta:
        model = SocialMediaLink
        fields = ['id', 'telegram', 'instagram', 'youtube', 'facebook', 'translations']

    def get_translations(self, obj):
        return {
            'uz': {
                'location': obj.location_uz,
            },
            'ru': {
                'location': obj.location_ru,
            },
            'en': {
                'location': obj.location_en,
            },
        }


class CourseRoadMapFieldSerializer(serializers.ModelSerializer):
    translations = serializers.SerializerMethodField()
    class Meta:
        model = CourseRoadMapField
        fields = ['id', 'road_map', 'translations']

    def get_translations(self, obj):
        return {
            'uz': {
                'info': obj.info_uz,
            },
            'ru': {
                'info': obj.info_ru,
            },
            'en': {
                'info': obj.info_en,
            },
        }


class CourseRoadMapSerializer(serializers.ModelSerializer):
    translations = serializers.SerializerMethodField()
    info = CourseRoadMapFieldSerializer(many=True)

    class Meta:
        model = CourseRoadMap
        fields = ['id', 'course', 'translations', 'info']

    def get_translations(self, obj):
        return {
            'uz': {
                'name': obj.name_uz,
            },
            'ru': {
                'name': obj.name_ru,
            },
            'en': {
                'name': obj.name_en,
            },
        }


class CourseSerializer(serializers.ModelSerializer):
    translations = serializers.SerializerMethodField()
    roadmap = CourseRoadMapSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'image', 'duration', 'translations', 'roadmap']

    def get_translations(self, obj):
        return {
            'uz': {
                'name': obj.name_uz,
                'description': obj.description_uz,
            },
            'ru': {
                'name': obj.name_ru,
                'description': obj.description_ru,
            },
            'en': {
                'name': obj.name_en,
                'description': obj.description_en,
            },
        }


class TeacherSerializer(serializers.ModelSerializer):
    translations = serializers.SerializerMethodField()
    class Meta:
        model = Teacher
        fields = ['id', 'image', 'instagram', 'telegram', 'facebook', 'video', 'translations']

    def get_translations(self, obj):
        return {
            'uz': {
                'full_name': obj.full_name_uz,
                'subject': obj.subject_uz,
                'about': obj.about_uz,
            },
            'ru': {
                'full_name': obj.full_name_ru,
                'subject': obj.subject_ru,
                'about': obj.about_ru,
            },
            'en': {
                'full_name': obj.full_name_en,
                'subject': obj.subject_en,
                'about': obj.about_en,
            },
        }


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = "__all__"


class BranchSerializer(serializers.ModelSerializer):
    translations = serializers.SerializerMethodField()
    class Meta:
        model = Branch
        fields = ['id', 'image', 'lat', 'lot', 'translations']
        
    def get_translations(self, obj):
        return {
            'uz':{
                'name':obj.name_uz,
                'about': obj.about_uz,
            },
            'ru':{
                'name':obj.name_ru,
                'about': obj.about_ru,
            },
            'en':{
                'name':obj.name_en,
                'about': obj.about_en,
            },
        }


class SubjectSerializer(serializers.ModelSerializer):
    translations = serializers.SerializerMethodField()
    class Meta:
        model = Subject
        fields = ['id', 'image', 'translations']
        
    def get_translations(self, obj):
        return {
            'uz': {
                'name': obj.name_uz
            },
            'ru': {
                'name': obj.name_ru
            },
            'en': {
                'name': obj.name_en
            },
        }


class QuizSerializer(serializers.ModelSerializer):
    translations = serializers.SerializerMethodField()
    subject = SubjectSerializer()
    class Meta:
        model = Quiz
        fields = ['id', 'correct_answer', 'difficulty', 'translations']
        
    def get_translations(self, obj):
        return {
            'uz': {
                'name': obj.name_uz,
                'answer1': obj.answer1_uz,
                'answer2': obj.answer2_uz,
                'answer3': obj.answer3_uz,
                'answer4': obj.answer4_uz,
            }, 
            'ru': {
                'name': obj.name_ru,
                'answer1': obj.answer1_ru,
                'answer2': obj.answer2_ru,
                'answer3': obj.answer3_ru,
                'answer4': obj.answer4_ru,
            },
            'en': {
                'name': obj.name_en,
                'answer1': obj.answer1_en,
                'answer2': obj.answer2_en,
                'answer3': obj.answer3_en,
                'answer4': obj.answer4_en,
            },
        }


class CertificateSerializer(serializers.ModelSerializer):
    translations = serializers.SerializerMethodField()
    subject = SubjectSerializer()
    class Meta:
        model = Certificate
        fields = ['id', 'image', 'level', 'subject', 'translations']
    
    def get_translations(self, obj):
        return {
            'uz':{
                'full_name':obj.full_name_uz
            },
            'ru':{
                'full_name': obj.full_name_ru
            },
            'en':{
                'full_name':obj.full_name_en
            }
                
        }
        
        
class RegisterImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterImage
        fields = "__all__"
        
        
class TestSerializer(serializers.ModelSerializer):
    translations = serializers.SerializerMethodField()
    class Meta:
        model = TestModel
        fields = ['id', 'translations']

    def get_translations(self, obj):
        return {
            "uz": {
                "title": obj.title_uz,
                "name": obj.name_uz,
                "info": obj.info_uz,
            },
            "ru": {
                "title": obj.title_ru,
                "name": obj.name_ru,
                "info": obj.info_ru,
            },
            "en": {
                "title": obj.title_en,
                "name": obj.name_en,
                "info": obj.info_en,
            },
        }