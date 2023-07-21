from django.db import models
from django.conf import settings

# from apps.account.models import Profile
from apps.main.models import Category, Tag
from ckeditor.fields import RichTextField


class Timestamp(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def image_path(instance, filename):
    return f"courses/{instance.title}/image/{filename}"


def file_path(instance, filename):
    return f"courses/{instance}/{filename}"


class Course(Timestamp):
    DIFFICULTY = (
        (0, 'Beginner'),
        (1, 'Intermediate'),
        (2, 'Advanced'),
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                               limit_choices_to={"role": 1})
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=221)
    body = RichTextField()
    image = models.ImageField(upload_to=image_path)
    difficulty = models.IntegerField(choices=DIFFICULTY, default=0)
    price = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Lesson(Timestamp):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=221)
    body = RichTextField()

    def __str__(self):
        return self.title


class LessonFiles(Timestamp):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    file = models.FileField(upload_to=file_path)
    is_main = models.BooleanField(default=False)


class SoldCourse(models.Model):
    profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={"role": 0})
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    is_free = models.BooleanField(default=False)
