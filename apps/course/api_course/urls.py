from django.urls import path
from . import views

urlpatterns = [
    path('list-create/', views.CourseListCreateAPIView.as_view()),
    path('rud/<int:pk>/', views.CourseRUDAPIView.as_view()),
    path('<int:course_id>/lessons/', views.LessonListCreateAPIView.as_view()),
    path('<int:course_id>/lessons/<int:pk>/', views.LessonRUDAPIView.as_view()),
    path('<int:course_id>/lessons/<int:pk>/files/', views.LessonFilesListCreateAPIView.as_view())
]
