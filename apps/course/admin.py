from django.contrib import admin
from .models import Lesson, LessonFiles, Course, SoldCourse


class LessonFilesInline(admin.TabularInline):
    model = LessonFiles
    extra = 1


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    inlines = (LessonFilesInline, )
    list_display = ['id', 'title', 'course']


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 0


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ['id', 'title']


@admin.register(SoldCourse)
class SoldCourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'course', 'profile']


@admin.register(LessonFiles)
class LessonFilesAdmin(admin.ModelAdmin):
    list_display = ['id', 'lesson']