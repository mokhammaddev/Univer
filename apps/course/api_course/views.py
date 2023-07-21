from rest_framework import generics, permissions
from .serializers import CourseGetSerializer, CoursePostSerializer, LessonSerializer, LessonPostSerializer, \
    LessonFilesSerializer, LessonFilesPostSerializer
from ..models import Course, Lesson, LessonFiles, SoldCourse


class CourseListCreateAPIView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/api/course/list-create/
    queryset = Course.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CourseGetSerializer
        return CoursePostSerializer


class CourseRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/api/course/rud/{course_id}/
    queryset = Course.objects.all()
    serializer_class = CourseGetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LessonListCreateAPIView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/api/course/{course_id}/lessons/
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(course_id=self.kwargs.get('course_id'))
        return qs

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return LessonPostSerializer
        return super().get_serializer_class()

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['course_id'] = self.kwargs.get('course_id')
        return ctx


class LessonRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/api/course/{course_id}/lessons/{lesson_id}/
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LessonFilesListCreateAPIView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/api/course/{course_id}/lessons/{lesson_id}/files/
    queryset = LessonFiles.objects.all()
    serializer_class = LessonFilesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(lesson_id=self.kwargs.get('lesson_id'))
        return qs

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return LessonFilesPostSerializer
        return super().get_serializer_class()

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['lesson_id'] = self.kwargs.get('lesson_id')
        return ctx
