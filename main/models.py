from django.db import models
from django.utils.translation import gettext_lazy as _


def tr_fields(field_type, *args, **kwargs):
    """
    Ko‘p tilli fieldlarni yaratadi (UZ, RU, EN) va har biriga mos verbose_name beradi.
    
    Misol:
        locals().update(tr_fields(models.CharField, max_length=255, name='title', verbose_name='Sarlavha'))
    """
    LANGS = {
        'uz': '🇺🇿 (Oʻzbekcha)',
        'ru': '🇷🇺 (Русский)',
        'en': '🇬🇧 (English)'
    }
    fields = {}

    base_verbose = kwargs.pop('verbose_name', kwargs.get('name', 'Field'))

    for lang, lang_label in LANGS.items():
        fields[f"{kwargs.get('name')}_{lang}"] = field_type(
            *args,
            verbose_name=f"{base_verbose} {lang_label}",
            **{k: v for k, v in kwargs.items() if k != 'name'}
        )

    return fields



class BaseModel(models.Model):
    created_at = models.DateTimeField(_('Yaratilgan vaqti'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Yangilangan vaqti'), auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']

    def __str__(self):
        return f"<{self.__class__.__name__} ({self.id})>"


class Banner(BaseModel):
    locals().update(tr_fields(models.CharField, name='title', max_length=150, verbose_name=_('Sarlavha')))
    locals().update(tr_fields(models.CharField, name='description', max_length=200, verbose_name=_('Izoh')))
    image = models.ImageField(_('Rasm'), upload_to='banner_photos/')

    def __str__(self):
        return self.title_uz

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
    locals().update(tr_fields(models.CharField, name='location', max_length=100, verbose_name=_('Manzil')))

    class Meta:
        verbose_name = _("Ijtimoiy tarmoq")
        verbose_name_plural = _("Ijtimoiy tarmoqlar")
        db_table = "social_links"
        ordering = ['-created_at']


class CourseRoadMapField(BaseModel):
    locals().update(tr_fields(models.TextField, name='info', verbose_name=_('Tavsif')))
    road_map = models.ForeignKey(to='CourseRoadMap', related_name='info', on_delete=models.CASCADE)

    def __str__(self):
        return self.info_uz

    class Meta:
        verbose_name = _("Yo‘l xaritasi matni")
        verbose_name_plural = _("Yo‘l xaritasi matnlari")
        db_table = "course_roadmap_field"
        ordering = ['-created_at']


class CourseRoadMap(BaseModel):
    locals().update(tr_fields(models.CharField, max_length=50, name='name', verbose_name=_('Nomi')))
    course = models.ForeignKey(to='Course', related_name='roadmap', on_delete=models.CASCADE)

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = _("Yo‘l xaritasi")
        verbose_name_plural = _("Yo‘l xaritalari")
        db_table = "course_roadmap"
        ordering = ['-created_at']


class Course(BaseModel):
    image = models.ImageField(_('Rasm'), upload_to='course_photos/')
    locals().update(tr_fields(models.CharField, max_length=50, name='name', verbose_name=_('Kurs nomi')))
    locals().update(tr_fields(models.TextField, name='description', verbose_name=_('Tavsif')))
    duration = models.IntegerField(_('Davomiyligi (oy)'))

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = _("Kurs")
        verbose_name_plural = _("Kurslar")
        db_table = "course"
        ordering = ['-created_at']


class Teacher(BaseModel):
    image = models.ImageField(_('Rasm'), upload_to='teacher_photos/')
    locals().update(tr_fields(models.CharField, max_length=100, name='full_name', verbose_name=_('F.I.Sh')))
    locals().update(tr_fields(models.CharField, max_length=50, name='subject', verbose_name=_('Fan')))
    locals().update(tr_fields(models.TextField, name='about', verbose_name=_('O‘qituvchi haqida')))

    instagram = models.URLField(_('Instagram'))
    telegram = models.URLField(_('Telegram'))
    facebook = models.URLField(_('Facebook'))
    video = models.URLField(_('Video havola'))

    def __str__(self):
        return self.full_name_uz

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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Aloqa")
        verbose_name_plural = _("Aloqalar")
        db_table = "contact_us"
        ordering = ['-created_at']


class Branch(BaseModel):
    locals().update(tr_fields(models.CharField, max_length=100, name='name', verbose_name=_('Filial nomi')))
    locals().update(tr_fields(models.TextField, name='about', verbose_name=_('Tavsif')))

    image = models.ImageField(_('Rasm'), upload_to='branch_photos/')
    lat = models.CharField(_('Latitude'), max_length=255)
    lot = models.CharField(_('Longitude'), max_length=255)

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = _("Filial")
        verbose_name_plural = _("Filiallar")
        db_table = "branch"
        ordering = ['-created_at']


class Subject(BaseModel):
    locals().update(tr_fields(models.CharField, max_length=50, name='name', verbose_name=_('Fan nomi')))
    image = models.ImageField(_('Rasm'), upload_to="Subject_photos")

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = _("Fan")
        verbose_name_plural = _("Fanlar")
        db_table = "subject"
        ordering = ['-created_at']


class Quiz(BaseModel):
    DIFFICULTY = (
        ("easy", "Oson"),
        ("medium", "O‘rta"),
        ("hard", "Qiyin"),
    )

    # === 3 TILDA MAYDONLAR ===
    locals().update(tr_fields(models.CharField, max_length=100, name='name', verbose_name=_('Savol')))
    locals().update(tr_fields(models.CharField, max_length=50, name='answer1', verbose_name=_('Variant 1')))
    locals().update(tr_fields(models.CharField, max_length=50, name='answer2', verbose_name=_('Variant 2')))
    locals().update(tr_fields(models.CharField, max_length=50, name='answer3', verbose_name=_('Variant 3')))
    locals().update(tr_fields(models.CharField, max_length=50, name='answer4', verbose_name=_('Variant 4')))

    ANSWER = (
        (1, "Variant 1"),
        (2, "Variant 2"),
        (3, "Variant 3"),
        (4, "Variant 4"),
    )

    correct_answer = models.IntegerField(_('To‘g‘ri javob'), choices=ANSWER)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, verbose_name=_("Fan"))

    difficulty = models.CharField(
        _('Qiyinchilik darajasi'),
        max_length=10,
        choices=DIFFICULTY,
        default="medium"
    )

    def __str__(self):
        # Default til sifatida o‘zbekcha nomni qaytaradi
        return self.name_uz

    class Meta:
        verbose_name = _("Test")
        verbose_name_plural = _("Testlar")
        db_table = "quiz"
        ordering = ['-created_at']


class Certificate(BaseModel):
    image = models.ImageField(_('Rasm'), upload_to='Certificate_photos/')
    locals().update(tr_fields(models.CharField, max_length=100, name='full_name', verbose_name=_('F.I.Sh')))

    level = models.CharField(_('Daraja'), max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name=_("Fan"))

    def __str__(self):
        return self.full_name_uz

    class Meta:
        verbose_name = _("Sertifikat")
        verbose_name_plural = _("Sertifikatlar")
        db_table = "certificate"
        ordering = ['-created_at']
        
        
class RegisterImage(BaseModel):
    image = models.ImageField(upload_to='register_photos/')


class TelegramAdmin(BaseModel):
    telegram_id = models.IntegerField()
    name = models.CharField(max_length=100, null=True, blank=True)
    


class TestModel(models.Model):
    locals().update(tr_fields(models.CharField, max_length=255, name='title'))
    locals().update(tr_fields(models.CharField, max_length=255, name='name'))
    locals().update(tr_fields(models.TextField, name='info'))

    def get_lang(self, field, lang='uz'):
        return getattr(self, f"{field}_{lang}", None)

    def __str__(self):
        return self.title_uz
