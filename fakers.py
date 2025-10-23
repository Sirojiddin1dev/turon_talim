import os
import django
import random
from faker import Faker

# Django sozlash
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'home.settings')
django.setup()

from main.models import (
    Banner, HomeStats, SocialMediaLink, Course, CourseRoadMap,
    CourseRoadMapField, Teacher, About, ContactUs, Branch,
    Subject, Quiz, Certificate
)

fake = Faker('uz_UZ')  # o‘zbekcha uslubdagi faker


def create_banners(n=100):
    for _ in range(n):
        Banner.objects.create(
            title=fake.sentence(nb_words=4),
            description=fake.text(max_nb_chars=100),
            image=f"banner_photos/{fake.file_name(extension='jpg')}"
        )


def create_home_stats(n=100):
    for _ in range(n):
        HomeStats.objects.create(
            students=random.randint(50, 500),
            year_exp=random.randint(1, 10),
            employment=random.randint(50, 100),
            university_student=random.randint(100, 300)
        )


def create_social_links(n=100):
    for _ in range(n):
        SocialMediaLink.objects.create(
            telegram=fake.url(),
            instagram=fake.url(),
            youtube=fake.url(),
            facebook=fake.url(),
            location=fake.address()
        )


def create_courses(n=100):
    for _ in range(n):
        Course.objects.create(
            image=f"course_photos/{fake.file_name(extension='jpg')}",
            name=fake.word().capitalize(),
            description=fake.text(max_nb_chars=200),
            duration=random.randint(3, 12)
        )


def create_course_roadmap(n=100):
    courses = list(Course.objects.all())
    if not courses:
        create_courses()
        courses = list(Course.objects.all())
    for _ in range(n):
        CourseRoadMap.objects.create(
            name=fake.sentence(nb_words=3),
            course=random.choice(courses)
        )


def create_course_roadmap_field(n=100):
    roadmaps = list(CourseRoadMap.objects.all())
    if not roadmaps:
        create_course_roadmap()
        roadmaps = list(CourseRoadMap.objects.all())
    for _ in range(n):
        CourseRoadMapField.objects.create(
            info=fake.text(max_nb_chars=150),
            road_maop=random.choice(roadmaps)
        )


def create_teachers(n=100):
    for _ in range(n):
        Teacher.objects.create(
            image=f"teacher_photos/{fake.file_name(extension='jpg')}",
            full_name=fake.name(),
            subject=fake.word().capitalize(),
            about=fake.text(max_nb_chars=200),
            instagram=fake.url(),
            telegram=fake.url(),
            facebook=fake.url(),
            video=fake.url()
        )


def create_about(n=100):
    for _ in range(n):
        About.objects.create(
            students=random.randint(100, 1000),
            exp=random.randint(1, 10),
            teachers=random.randint(5, 50),
            graduates=random.randint(50, 500),
            image=f"about_photos/{fake.file_name(extension='jpg')}",
            lat=str(fake.latitude()),
            lot=str(fake.longitude())
        )


def create_contacts(n=100):
    for _ in range(n):
        ContactUs.objects.create(
            name=fake.first_name(),
            email=fake.email(),
            message=fake.text(max_nb_chars=200)
        )


def create_branches(n=100):
    for _ in range(n):
        Branch.objects.create(
            name=fake.city(),
            about=fake.text(max_nb_chars=150),
            image=f"branch_photos/{fake.file_name(extension='jpg')}",
            lat=str(fake.latitude()),
            lot=str(fake.longitude())
        )


def create_subjects(n=100):
    for _ in range(n):
        Subject.objects.create(
            name=fake.word().capitalize(),
            image=f"Subject_photos/{fake.file_name(extension='jpg')}"
        )


def create_quizzes(n=100):
    subjects = list(Subject.objects.all())
    if not subjects:
        create_subjects()
        subjects = list(Subject.objects.all())

    for _ in range(n):
        Quiz.objects.create(
            name=fake.sentence(nb_words=5),
            answer1=fake.word(),
            answer2=fake.word(),
            answer3=fake.word(),
            answer4=fake.word(),
            correct_answer=random.randint(1, 4),
            subject=random.choice(subjects)
        )


def create_certificates(n=100):
    subjects = list(Subject.objects.all())
    if not subjects:
        create_subjects()
        subjects = list(Subject.objects.all())

    for _ in range(n):
        Certificate.objects.create(
            image=f"Certificate_photos/{fake.file_name(extension='jpg')}",
            full_name=fake.name(),
            level=random.choice(["Boshlang‘ich", "O‘rta", "Yuqori"]),
            subject=random.choice(subjects)
        )


if __name__ == '__main__':
    print("Fake ma’lumotlar yaratilmoqda...")

    create_banners()
    create_home_stats()
    create_social_links()
    create_courses()
    create_course_roadmap()
    create_course_roadmap_field()
    create_teachers()
    create_about()
    create_contacts()
    create_branches()
    create_subjects()
    create_quizzes()
    create_certificates()

    print("✅ Barcha ma’lumotlar muvaffaqiyatli yaratildi!")
