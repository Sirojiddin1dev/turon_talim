import os
import django
import random
import requests
from io import BytesIO
from django.core.files.base import ContentFile

# Django sozlash — loyihang settings modulini kiriting:
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "home.settings")
django.setup()

from main.models import (
    Banner, Course, CourseRoadMap, CourseRoadMapField,
    Teacher, Subject, Certificate, Branch
)
from faker import Faker

fake_uz = Faker("uz_UZ")
fake_ru = Faker("ru_RU")
fake_en = Faker("en_US")

def get_real_image(category="default"):
    """
    Picsum’dan random rasm olib beradi.
    """
    try:
        url = f"https://picsum.photos/seed/{random.randint(1,10000)}/600/400"
        resp = requests.get(url)
        if resp.status_code == 200:
            # nomni category + random raqam bilan beramiz
            fname = f"{category}_{random.randint(1000,9999)}.jpg"
            return ContentFile(resp.content, name=fname)
    except Exception as e:
        print("Image error:", e)
    return None

def create_subjects(n=5):
    subs = []
    for i in range(n):
        sub = Subject.objects.create(
            name_uz=fake_uz.word().capitalize(),
            name_ru=fake_ru.word().capitalize(),
            name_en=fake_en.word().capitalize(),
            image=get_real_image("subject")
        )
        subs.append(sub)
    print("Subjects done:", len(subs))
    return subs

def create_courses(n=5):
    courses = []
    for i in range(n):
        c = Course.objects.create(
            name_uz=fake_uz.word().capitalize(),
            name_ru=fake_ru.word().capitalize(),
            name_en=fake_en.word().capitalize(),
            description_uz=fake_uz.text(80),
            description_ru=fake_ru.text(80),
            description_en=fake_en.text(80),
            image=get_real_image("course"),
            duration=random.randint(3, 12),
        )
        courses.append(c)
    print("Courses done:", len(courses))
    return courses

def create_roadmaps(courses, n=3):
    rms = []
    for course in courses:
        for _ in range(n):
            rm = CourseRoadMap.objects.create(
                course=course,
                name_uz=fake_uz.sentence(nb_words=3),
                name_ru=fake_ru.sentence(nb_words=3),
                name_en=fake_en.sentence(nb_words=3),
            )
            rms.append(rm)
    print("Roadmaps done:", len(rms))
    return rms

def create_roadmap_fields(roadmaps, n=3):
    for rm in roadmaps:
        for _ in range(n):
            CourseRoadMapField.objects.create(
                road_map=rm,
                info_uz=fake_uz.text(50),
                info_ru=fake_ru.text(50),
                info_en=fake_en.text(50)
            )
    print("RoadmapFields created")

def create_teachers(n=5):
    for _ in range(n):
        Teacher.objects.create(
            full_name_uz=fake_uz.name(),
            full_name_ru=fake_ru.name(),
            full_name_en=fake_en.name(),
            subject_uz=fake_uz.word().capitalize(),
            subject_ru=fake_ru.word().capitalize(),
            subject_en=fake_en.word().capitalize(),
            about_uz=fake_uz.text(80),
            about_ru=fake_ru.text(80),
            about_en=fake_en.text(80),
            image=get_real_image("teacher"),
            instagram=f"https://instagram.com/{fake_en.user_name()}",
            telegram=f"https://t.me/{fake_en.user_name()}",
            facebook=f"https://facebook.com/{fake_en.user_name()}",
            video="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        )
    print("Teachers created")

def create_certificates(subjects, n=5):
    for _ in range(n):
        Certificate.objects.create(
            full_name_uz=fake_uz.name(),
            full_name_ru=fake_ru.name(),
            full_name_en=fake_en.name(),
            level=random.choice(["Boshlang‘ich", "O‘rta", "Yuqori"]),
            subject=random.choice(subjects),
            image=get_real_image("certificate")
        )
    print("Certificates done")

def create_branches(n=5):
    for _ in range(n):
        Branch.objects.create(
            name_uz=fake_uz.city(),
            name_ru=fake_ru.city(),
            name_en=fake_en.city(),
            about_uz=fake_uz.text(100),
            about_ru=fake_ru.text(100),
            about_en=fake_en.text(100),
            image=get_real_image("branch"),
            lat=str(fake_en.latitude()),
            lot=str(fake_en.longitude())
        )
    print("Branches done")

if __name__ == "__main__":
    print("Populating with real images and coherent data...")
    subs = create_subjects(5)
    courses = create_courses(5)
    rms = create_roadmaps(courses, 2)
    create_roadmap_fields(rms, 2)
    create_teachers(5)
    create_certificates(subs, 5)
    create_branches(5)
    print("Done!")
