from django.urls import path, include
from .views import course, detail, lesson_detail


urlpatterns = [
    path('course/', course, name='course'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('lesson_detail/<int:course_id>/<int:pk>/', lesson_detail, name='lesson_detail'),
]
