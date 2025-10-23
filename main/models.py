from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(_('Yaratilgan vaqti'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Yangilangan vaqti'), auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']

    def __str__(self):
        return f"<{self.__class__.__name__} ({self.id})>"


class Banner(BaseModel):
    title = models.CharField(_('Sarlavha'), max_length=150)
    description = models.CharField(_('Izoh'), max_length=200)
    image = models.ImageField(_('Rasm'), upload_to='banner_photos/')

    class Meta:
        verbose_name = _("Banner")
        verbose_name_plural = _("Bannerlar")
        db_table = "banner"
        ordering = ['-created_at']


class HomeStats(BaseModel):
    students = models.IntegerField(_('Talabalar soni'))
    year_exp = models.IntegerField(_('Tajriba yili'))
    employment = models.IntegerField(_('Ishga joylashish foizi'))
    university_student = models.IntegerField(_('Universitet talabasi'))

    class Meta:
        verbose_name = _("Statistika")
        verbose_name_plural = _("Statistikalar")
        db_table = "home_stats"
        ordering = ['-created_at']


class SocialMediaLink(BaseModel):
    telegram = models.URLField(_('Telegram'))
    instagram = models.URLField(_('Instagram'))
    youtube = models.URLField(_('YouTube'))
    facebook = models.URLField(_('Facebook'))
    location = models.CharField(_('Manzil'), max_length=100)

    class Meta:
        verbose_name = _("Ijtimoiy tarmoq")
        verbose_name_plural = _("Ijtimoiy tarmoqlar")
        db_table = "social_links"
        ordering = ['-created_at']


class CourseRoadMapField(BaseModel):
    info = models.TextField(_('Tavsif'))
    road_maop = models.ForeignKey(to='CourseRoadMap', related_name='course_road_map', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Yo‘l xaritasi matni")
        verbose_name_plural = _("Yo‘l xaritasi matnlari")
        db_table = "course_roadmap_field"
        ordering = ['-created_at']


class CourseRoadMap(BaseModel):
    name = models.CharField(_('Nomi'), max_length=50)
    course = models.ForeignKey(to='Course', related_name='course', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Yo‘l xaritasi")
        verbose_name_plural = _("Yo‘l xaritalari")
        db_table = "course_roadmap"
        ordering = ['-created_at']


class Course(BaseModel):
    image = models.ImageField(_('Rasm'), upload_to='course_photos/')
    name = models.CharField(_('Kurs nomi'), max_length=50)
    description = models.TextField(_('Tavsif'))
    duration = models.IntegerField(_('Davomiyligi (oy)'))

    class Meta:
        verbose_name = _("Kurs")
        verbose_name_plural = _("Kurslar")
        db_table = "course"
        ordering = ['-created_at']


class Teacher(BaseModel):
    image = models.ImageField(_('Rasm'), upload_to='teacher_photos/')
    full_name = models.CharField(_('F.I.Sh'), max_length=100)
    subject = models.CharField(_('Fan'), max_length=50)
    about = models.TextField(_('O‘qituvchi haqida'))
    instagram = models.URLField(_('Instagram'))
    telegram = models.URLField(_('Telegram'))
    facebook = models.URLField(_('Facebook'))
    video = models.URLField(_('Video havola'))

    class Meta:
        verbose_name = _("O‘qituvchi")
        verbose_name_plural = _("O‘qituvchilar")
        db_table = "teacher"
        ordering = ['-created_at']


class About(BaseModel):
    students = models.IntegerField(_('Talabalar soni'))
    exp = models.IntegerField(_('Tajriba yili'))
    teachers = models.IntegerField(_('O‘qituvchilar soni'))
    graduates = models.IntegerField(_('Bitiruvchilar soni'))
    image = models.ImageField(_('Rasm'), upload_to='about_photos/')
    lat = models.CharField(_('Latitude'), max_length=255)
    lot = models.CharField(_('Longitude'), max_length=255)

    class Meta:
        verbose_name = _("Biz haqimizda")
        verbose_name_plural = _("Biz haqimizda (tartiblar)")
        db_table = "about"
        ordering = ['-created_at']


class ContactUs(BaseModel):
    name = models.CharField(_('Ism'), max_length=100)
    email = models.CharField(_('Email'), max_length=255)
    message = models.TextField(_('Xabar'))

    class Meta:
        verbose_name = _("Aloqa")
        verbose_name_plural = _("Aloqalar")
        db_table = "contact_us"
        ordering = ['-created_at']


class Branch(BaseModel):
    name = models.CharField(_('Filial nomi'), max_length=100)
    about = models.TextField(_('Tavsif'))
    image = models.ImageField(_('Rasm'), upload_to='branch_photos/')
    lat = models.CharField(_('Latitude'), max_length=255)
    lot = models.CharField(_('Longitude'), max_length=255)

    class Meta:
        verbose_name = _("Filial")
        verbose_name_plural = _("Filiallar")
        db_table = "branch"
        ordering = ['-created_at']


class Subject(BaseModel):
    name = models.CharField(_('Fan nomi'), max_length=50)
    image = models.ImageField(_('Rasm'), upload_to="Subject_photos")

    class Meta:
        verbose_name = _("Fan")
        verbose_name_plural = _("Fanlar")
        db_table = "subject"
        ordering = ['-created_at']


class Quiz(BaseModel):
    name = models.CharField(_('Savol'), max_length=100)
    answer1 = models.CharField(_('Variant 1'), max_length=50)
    answer2 = models.CharField(_('Variant 2'), max_length=50)
    answer3 = models.CharField(_('Variant 3'), max_length=50)
    answer4 = models.CharField(_('Variant 4'), max_length=50)

    ANSWER = (
        (1, "Variant 1"),
        (2, "Variant 2"),
        (3, "Variant 3"),
        (4, "Variant 4"),
    )

    correct_answer = models.IntegerField(_('To‘g‘ri javob'), choices=ANSWER)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name=_("Fan"))

    class Meta:
        verbose_name = _("Test")
        verbose_name_plural = _("Testlar")
        db_table = "quiz"
        ordering = ['-created_at']


class Certificate(BaseModel):
    image = models.ImageField(_('Rasm'), upload_to='Certificate_photos/')
    full_name = models.CharField(_('F.I.Sh'), max_length=100)
    level = models.CharField(_('Daraja'), max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name=_("Fan"))

    class Meta:
        verbose_name = _("Sertifikat")
        verbose_name_plural = _("Sertifikatlar")
        db_table = "certificate"
        ordering = ['-created_at']
