from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import *
from .serializers import *
from .bot import send_message_admin


from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Quiz
from .serializers import QuizSerializer
import random
from .utils import handle_request, AResponse as Response

@swagger_auto_schema(
    method='get',
    responses={200: BannerSerializer(many=True)},
    operation_description="Bannerlar ro‘yhatini olish"
)
@api_view(['GET'])
@handle_request
def banner_list(request):
    banners = Banner.objects.all().order_by('-id')[:6]
    serializer = BannerSerializer(banners, many=True)
    return Response(serializer.data)


@swagger_auto_schema(
    method='get',
    responses={200: HomeStatsSerializer(many=True)},
    operation_description="Home statistikalar"
)
@api_view(['GET'])
@handle_request
def home_stats(request):
    stats = HomeStats.objects.last()
    serializer = HomeStatsSerializer(stats)
    return Response(serializer.data)


@swagger_auto_schema(
    method='get',
    responses={200: SocialMediaLinkSerializer(many=True)},
    operation_description="Ijtimoiy tarmoqlar linklari"
)
@api_view(['GET'])
@handle_request
def social_links(request):
    links = SocialMediaLink.objects.last()
    serializer = SocialMediaLinkSerializer(links)
    return Response(serializer.data)


@swagger_auto_schema(
    method='get',
    responses={200: CourseSerializer(many=True)},
    operation_description="Kurslar ro‘yxati"
)
@api_view(['GET'])
@handle_request
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
@handle_request
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
@handle_request
def about_list(request):
    data = About.objects.last()
    serializer = AboutSerializer(data)
    return Response(serializer.data)


@swagger_auto_schema(
    method='post',
    request_body=ContactUsSerializer,
    responses={201: ContactUsSerializer()},
    operation_description="Kontakt xabar jo‘natish"
)
@api_view(['POST'])
@handle_request
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
@handle_request
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
@handle_request
def subject_list(request):
    subjects = Subject.objects.all()
    serializer = SubjectSerializer(subjects, many=True)
    return Response(serializer.data)


@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('subject_id', openapi.IN_QUERY, description="Fan ID", type=openapi.TYPE_INTEGER),
    ],
    responses={200: QuizSerializer(many=True)},
    operation_description="Fan bo‘yicha 7 ta qiyin, 7 ta o‘rta, 6 ta oson testni random tartibda qaytaradi"
)
@api_view(['GET'])
@handle_request
def quiz_list(request):
    subject_id = request.GET.get('subject_id')
    if not subject_id:
        return Response({"error": "subject_id kerak"}, status=400)

    # subject_id bo‘yicha 30 ta random quiz tanlaymiz
    quizzes = list(Quiz.objects.filter(subject_id=subject_id).order_by('?')[:30])

    serializer = QuizSerializer(quizzes, many=True)
    return Response({
        "count": len(quizzes),
        "results": serializer.data
    })



# ========================= QUIZ RESULT =========================

@swagger_auto_schema(
    method='post',
    operation_description="Quiz natijalarini tekshiradi va tildan kelib chiqib savollarni qaytaradi",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'subject_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Fan ID'),
            'lang': openapi.Schema(type=openapi.TYPE_STRING, description="Til (uz, ru, en)", default="uz"),
            'answers': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'quiz_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Quiz ID'),
                        'selected': openapi.Schema(type=openapi.TYPE_INTEGER, description='Tanlangan javob (1–4)')
                    }
                )
            )
        },
        required=['subject_id', 'answers']
    ),
    responses={200: 'Natijalar qaytariladi'}
)
@api_view(['POST'])
def quiz_result(request):
    subject_id = request.data.get('subject_id')
    answers = request.data.get('answers', [])
    lang = request.data.get('lang', 'uz')

    if lang not in ['uz', 'ru', 'en']:
        lang = 'uz'

    if not subject_id or not answers:
        return Response({"error": "subject_id va answers kerak"}, status=400)

    total = len(answers)
    correct = 0
    wrong = 0
    detailed_results = []

    for item in answers:
        try:
            quiz = Quiz.objects.get(id=item['quiz_id'], subject_id=subject_id)
            selected = int(item['selected'])
            is_correct = (quiz.correct_answer == selected)

            if is_correct:
                correct += 1
            else:
                wrong += 1

            # Dinamik tilga mos field nomlari
            name_field = f"name_{lang}"
            answer_fields = {str(i): getattr(quiz, f"answer{i}_{lang}") for i in range(1, 5)}

            detailed_results.append({
                "quiz_id": quiz.id,
                "question": getattr(quiz, name_field),
                "selected": selected,
                "correct_answer": quiz.correct_answer,
                "is_correct": is_correct,
                "answers": answer_fields
            })
        except Quiz.DoesNotExist:
            continue

    percentage = round((correct / total) * 100, 2)
    subject_name, group_result = detect_group(subject_id, percentage)

    return Response({
        "subject_id": subject_id,
        "subject_name": subject_name,
        "total_questions": total,
        "correct": correct,
        "wrong": wrong,
        "percentage": percentage,
        "group_result": group_result,
        "language": lang,
        "results": detailed_results
    })



# ========================= DARAJA ANIQLASH FUNKSIYASI =========================

def detect_group(subject_id, percentage):
    subject_id = int(subject_id)
    subject_map = {
        # 1. Ingliz tili
        1: {
            "name": "Ingliz tili",
            "levels": [
                (0, 20, "Starter"),
                (21, 40, "Beginner"),
                (41, 60, "Elementary"),
                (61, 75, "Pre-Intermediate"),
                (76, 90, "Intermediate"),
                (91, 100, "IELTS")
            ]
        },
        # 2. Rus tili
        2: {"name": "Rus tili", "levels": [(0, 40, "Boshlang‘ich"), (41, 75, "O‘rta"), (76, 100, "Yuqori (CEFR)")]} ,
        # 3. Arab tili
        3: {"name": "Arab tili", "levels": [(0, 40, "Boshlang‘ich"), (41, 75, "O‘rta"), (76, 100, "Yuqori (CEFR)")]} ,
        # 4. Koreys tili
        4: {"name": "Koreys tili", "levels": [(0, 40, "Boshlang‘ich"), (41, 75, "O‘rta"), (76, 100, "Yuqori (TOPIK)")]} ,
        # 5. Nemis tili
        5: {"name": "Nemis tili", "levels": [(0, 40, "Boshlang‘ich"), (41, 75, "O‘rta"), (76, 100, "Yuqori (TOEFL)")]} ,
        # 6. Matematika
        6: {"name": "Matematika", "levels": [(0, 40, "Boshlang‘ich"), (41, 75, "O‘rta"), (76, 100, "Yuqori (Milliy sertifikat)")]} ,
        # 7. Kimyo
        7: {"name": "Kimyo", "levels": [(0, 40, "Boshlang‘ich"), (41, 75, "O‘rta"), (76, 100, "Yuqori (Milliy sertifikat)")]} ,
        # 8. Biologiya
        8: {"name": "Biologiya", "levels": [(0, 40, "Boshlang‘ich"), (41, 75, "O‘rta"), (76, 100, "Yuqori (Milliy sertifikat)")]} ,
        # 9. IT Dasturlash
        9: {
            "name": "IT Dasturlash",
            "levels": [
                (0, 15, "HTML"),
                (16, 30, "CSS"),
                (31, 45, "Media/SCSS"),
                (46, 60, "JavaScript"),
                (61, 80, "API"),
                (81, 100, "Python / Node.js")
            ]
        }
    }

    # Agar fan mavjud bo‘lmasa — umumiy 3 darajali tizim
    subject = subject_map.get(subject_id)
    if not subject:
        subject = {
            "name": f"Nomaʼlum fan (ID {subject_id})",
            "levels": [
                (0, 40, "Boshlang‘ich"),
                (41, 75, "O‘rta"),
                (76, 100, "Yuqori (Umumiy)")
            ]
        }

    for low, high, level in subject["levels"]:
        if low <= percentage <= high:
            return (subject["name"], level)

    return (subject["name"], "Daraja aniqlanmadi")


@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('subject_id', openapi.IN_QUERY, description="fanlar idsini kirit", type=openapi.TYPE_STRING)
    ],
    responses={200: CertificateSerializer(many=True)},
    operation_description="Sertifikatlarni topish"
)
@api_view(['GET'])
@handle_request
def certificate_search(request):
    subject_id = request.GET.get('subject_id', '')
    if subject_id:
        cert = Certificate.objects.filter(subject=subject_id)
    else:
        cert = Certificate.objects.all()
    serializer = CertificateSerializer(cert, many=True)
    return Response(serializer.data)


@swagger_auto_schema(
    method='get',
    operation_description="So‘nggi 5 ta ro‘yxatdan o‘tish rasmlarini qaytaradi. Rasm ma'lumotlari `RegisterImageSerializer` orqali seriyalanadi.",
    responses={
        200: openapi.Response(
            description="So‘nggi 5 ta rasm muvaffaqiyatli qaytarildi",
            examples={
                "application/json": [
                    {
                        "id": 12,
                        "image": "https://example.com/media/register/img1.jpg",
                        "title": "Ro‘yxatdan o‘tish banner 1",
                        "created_at": "2025-10-28T17:30:12Z"
                    },
                    {
                        "id": 11,
                        "image": "https://example.com/media/register/img2.jpg",
                        "title": "Ro‘yxatdan o‘tish banner 2",
                        "created_at": "2025-10-27T20:12:44Z"
                    }
                ]
            }
        ),
        500: openapi.Response(description="Server xatosi")
    }
)
@api_view(['GET'])
@handle_request
def register_images(request):
    images = RegisterImage.objects.all().order_by('-id')[:5]
    ser = RegisterImageSerializer(images, many=True)
    return Response(ser.data)



@swagger_auto_schema(
    method='post',
    operation_description="Yangi foydalanuvchini ro'yxatdan o'tkazish, biz bilan bog'lanish yoki IELTS mock topshirish uchun universal endpoint.",
    manual_parameters=[
        openapi.Parameter(
            'action', openapi.IN_PATH,
            description="Amal turi: `register`, `contactus`, yoki `mock`",
            type=openapi.TYPE_STRING,
            required=True,
            enum=['register', 'contactus', 'mock']
        ),
    ],
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            # register
            'name': openapi.Schema(type=openapi.TYPE_STRING, description="Foydalanuvchi ismi"),
            'age': openapi.Schema(type=openapi.TYPE_INTEGER, description="Yoshi (faqat `register` uchun)"),
            'phone': openapi.Schema(type=openapi.TYPE_STRING, description="Telefon raqami (register va mock uchun)"),
            # contactus
            'email': openapi.Schema(type=openapi.TYPE_STRING, description="Email manzil (`contactus` uchun)"),
            'message': openapi.Schema(type=openapi.TYPE_STRING, description="Xabar (`contactus` uchun)"),
            # mock
            'subject': openapi.Schema(type=openapi.TYPE_STRING, description="Fan nomi (`mock` uchun)"),
        },
        required=['name'],
        example={
            "action": "register",
            "name": "Muxriddin",
            "age": 25,
            "phone": "+998901234567"
        }
    ),
    responses={
        200: openapi.Response("✅ Xabar muvaffaqiyatli yuborildi", examples={"application/json": "Amal muvaffaqiyatli bajarildi!"}),
        404: openapi.Response("❌ Noto‘g‘ri action qiymati", examples={"application/json": {
            "error": "Nomalum Metod\nYuborilishi kerak: \"register\", \"mock\", \"contactus\""
        }})
    }
)
@api_view(['POST'])
@handle_request
def send_register(request, action):
    if action == 'register':
        name = request.data.get('name')
        age = request.data.get('age')
        phone = request.data.get('phone')
        text = f"""
🆕Yangi <b>Ro'yxatdan O'tish!</b>

👤 <b>Ismi:</b> {name}
🎂 <b>Yoshi:</b> {age}
📞 <b>Telefon raqami:</b> {phone}

"""
    elif action == 'contactus':
        name = request.data.get('name')
        email = request.data.get('email')
        message = request.data.get('message')
        text = f"""
🆕Yangi <b>Bog'lanish!</b>

👤 <b>Ismi:</b> {name}
📧 <b>Email:</b> {email}
💬 <b>Habari:</b> {message}

"""
    elif action == 'mock':
        name = request.data.get('name')
        phone = request.data.get('phone')
        subject = request.data.get('subject')
        text = f"""
🆕Yangi <b>ILTS Mock topshirish!</b>       

👤 <b>Ismi:</b> {name}
📞 <b>Telefon raqami:</b> {phone} 
📕 <b>Fani:</b> {subject}     
        """
        
    else:
        return Response(error='Nomalum Metod\nYuborilishi kerak: "register", "mock", "contactus"', status_code=status.HTTP_404_NOT_FOUND)
    send_message_admin(text)
    return Response('Amal muvaffaqiyatli bajarildi!')
    
    
    

@api_view(['GET'])
@handle_request
def test_view(request):
    t = TestModel.objects.all()
    ser = TestSerializer(t, many=True)
    return Response(ser.data)