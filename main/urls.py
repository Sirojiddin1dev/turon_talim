from django.urls import path
from .views import *

urlpatterns = [
    path('banners/', banner_list),
    path('home-stats/', home_stats),
    path('social-links/', social_links),
    path('courses/', course_list),
    path('teachers/', teacher_list),
    path('about/', about_list),
    path('contact/', contact_us),
    path('branches/', branch_list),
    path('subjects/', subject_list),
    path('quizzes/', quiz_list),
    path('quiz-result/', quiz_result),
    path('certificates/', certificate_search),
    
    path('send_register/<str:action>/', send_register)
]
