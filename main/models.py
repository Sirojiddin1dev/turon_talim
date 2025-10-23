from django.db import models
from django.utils.translation import gettext_lazy as _



class BaseModel(models.Model):
    created_at = models.DateTimeField(_('Yaratilgan vaqti'), auto_now_add=True)
    updated_at = models.DateTimeField(_("Yangilangan vaqti"), auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']
        
    def __str__(self):
        return f"<{self.__class__.__name__} ({self.id})>"
    
    
class Banner(BaseModel):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='banner_photos/')

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = 'Bannerlar'
        

class HomeStats(BaseModel):
    students = models.IntegerField()
    year_exp = models.IntegerField()
    employment = models.IntegerField()
    university_student = models.IntegerField()
    
    
    
class SocialMediaLink(BaseModel):
    telegram = models.URLField()
    instagram = models.URLField()
    youtube = models.URLField()
    facebook = models.URLField()
    location = models.CharField(max_length=100)


class CourseRoadMapField(BaseModel):
    info = models.TextField()


class CourseRoadMap(BaseModel):
    name = models.CharField(max_length=50)
    info = models.ManyToManyField(CourseRoadMapField, related_name='roadmapfield')
   
    
class Course(BaseModel):
    image = models.ImageField(upload_to='course_photos/')
    name = models.CharField(max_length=50)
    description = models.TextField()
    duration = models.IntegerField()
    roadmap = models.ManyToManyField(CourseRoadMap, related_name='roadmap')
    
    
    
class Teacher(BaseModel):
    image = models.ImageField(upload_to='teacher_photos/')
    full_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    about = models.TextField()
    instagram = models.URLField()
    telegram = models.URLField()
    facebook = models.URLField()
    
    video = models.URLField()
    
    

class About(BaseModel):
    students = models.IntegerField()
    exp = models.IntegerField()
    teachers = models.IntegerField()
    graduates = models.IntegerField()
    image = models.ImageField(upload_to='about_photos/')
    
    lat = models.CharField(max_length=255)
    lot = models.CharField(max_length=255)
    
    
class ContactUs(BaseModel):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    message = models.TextField()
    

class Branch(BaseModel):
    name = models.CharField(max_length=100)
    about = models.TextField()
    image = models.ImageField(upload_to='branch_photos/')
    
    lat = models.CharField(max_length=255)
    lot = models.CharField(max_length=255)
    
    

    

    
    
    
    

    
    


   