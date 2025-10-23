from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import *
from .serializers import *


@swagger_auto_schema(
    method='get',
    responses={200: BannerSerializer(many=True)},
    operation_description="Bannerlar ro‘yhatini olish"
)
@api_view(['GET'])
def banner_list(request):
    banners = Banner.objects.all()
    serializer = BannerSerializer(banners, many=True)
    return Response(serializer.data)


@swagger_auto_schema(
    method='get',
    responses={200: HomeStatsSerializer(many=True)},
    operation_description="Home statistikalar"
)
@api_view(['GET'])
def home_stats(request):
    stats = HomeStats.objects.all()
    serializer = HomeStatsSerializer(stats, many=True)
    return Response(serializer.data)


@swagger_auto_schema(
    method='get',
    responses={200: SocialMediaLinkSerializer(many=True)},
    operation_description="Ijtimoiy tarmoqlar linklari"
)
@api_view(['GET'])
def social_links(request):
    links = SocialMediaLink.objects.all()
    serializer = SocialMediaLinkSerializer(links, many=True)
    return Response(serializer.data)


@swagger_auto_schema(
    method='get',
    responses={200: CourseSerializer(many=True)},
    operation_description="Kurslar ro‘yxati"
)
@api_view(['GET'])
def course_list(request):
    course = Course.objects.all()
    serializer = CourseSerializer(course, many=True)
    return Response(serializer.data)


@swagger_auto_schema(
    method='get',
    responses={200: TeacherSerializer(many=True)},
    operation_description="O‘qituvchilar ro‘yxati"
)
@api_view(['GET'])
def teacher_list(request):
    teachers = Teacher.objects.all()
    serializer = TeacherSerializer(teachers, many=True)
    return Response(serializer.data)


@swagger_auto_schema(
    method='get',
    responses={200: AboutSerializer(many=True)},
    operation_description="Biz haqimizda maʼlumotlar"
)
@api_view(['GET'])
def about_list(request):
    data = About.objects.all()
    serializer = AboutSerializer(data, many=True)
    return Response(serializer.data)


@swagger_auto_schema(
    method='post',
    request_body=ContactUsSerializer,
    responses={201: ContactUsSerializer()},
    operation_description="Kontakt xabar jo‘natish"
)
@api_view(['POST'])
def contact_us(request):
    serializer = ContactUsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@swagger_auto_schema(
    method='get',
    responses={200: BranchSerializer(many=True)},
    operation_description="Filiallar ro‘yxati"
)
@api_view(['GET'])
def branch_list(request):
    branch = Branch.objects.all()
    serializer = BranchSerializer(branch, many=True)
    return Response(serializer.data)


@swagger_auto_schema(
    method='get',
    responses={200: SubjectSerializer(many=True)},
    operation_description="Fanlar ro‘yxati"
)
@api_view(['GET'])
def subject_list(request):
    subjects = Subject.objects.all()
    serializer = SubjectSerializer(subjects, many=True)
    return Response(serializer.data)


@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('subject_id', openapi.IN_QUERY, description="Fan ID", type=openapi.TYPE_INTEGER)
    ],
    responses={200: QuizSerializer(many=True)},
    operation_description="Testlar ro‘yxati (subject_id bo‘yicha)"
)
@api_view(['GET'])
def quiz_list(request):
    subject_id = request.GET.get('subject_id')
    quiz = Quiz.objects.filter(subject_id=subject_id) if subject_id else Quiz.objects.all()
    serializer = QuizSerializer(quiz, many=True)
    return Response(serializer.data)


@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('subject_id', openapi.IN_QUERY, description="fanlar idsini kirit", type=openapi.TYPE_STRING)
    ],
    responses={200: CertificateSerializer(many=True)},
    operation_description="Sertifikatlarni topish"
)
@api_view(['GET'])
def certificate_search(request):
    subject_id = request.GET.get('subject_id', '')
    cert = Certificate.objects.filter(subject=subject_id)
    serializer = CertificateSerializer(cert, many=True)
    return Response(serializer.data)


