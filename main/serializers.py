from rest_framework import serializers
from .models import (
    Banner, HomeStats, SocialMediaLink, CourseRoadMapField, CourseRoadMap,
    Course, Teacher, About, ContactUs, Branch, Subject, Quiz, Certificate
)

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


class HomeStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeStats
        fields = "__all__"


class SocialMediaLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLink
        fields = "__all__"


class CourseRoadMapFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseRoadMapField
        fields = "__all__"


class CourseRoadMapSerializer(serializers.ModelSerializer):
    info = CourseRoadMapFieldSerializer(many=True)

    class Meta:
        model = CourseRoadMap
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    roadmap = CourseRoadMapSerializer(many=True)

    class Meta:
        model = Course
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = "__all__"


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = "__all__"


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = "__all__"
