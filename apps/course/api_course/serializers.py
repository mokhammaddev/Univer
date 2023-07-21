from rest_framework import serializers
from ..models import Course, Lesson, LessonFiles, SoldCourse
from ...main.api_main.serializers import CategorySerializer, TagSerializer
from ...account.api_account.serializers import MyAccountSerializer


class CourseGetSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tag = TagSerializer(read_only=True, many=True)
    author = MyAccountSerializer(read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'author', 'category', 'title', 'body', 'image', 'difficulty', 'get_difficulty_display',
                  'price', 'tag', 'created_date']


class CoursePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'author', 'category', 'title', 'body', 'image', 'difficulty', 'get_difficulty_display',
                  'price', 'tag', 'created_date']
        extra_kwargs = {
            "author": {"read_only": True},
            "image": {"required": False},
        }

    def create(self, validated_data):
        request = self.context['request']
        user_id = request.user.id
        instance = super().create(validated_data)
        instance.author_id = user_id
        instance.save()
        return instance


class LessonFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonFiles
        fields = ['id', 'lesson', 'file', 'is_main', 'created_date']


class LessonFilesPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonFiles
        fields = ['id', 'lesson', 'file', 'is_main', 'created_date']

    def create(self, validated_data):
        lesson_id = self.context['lesson_id']
        instance = LessonFiles(**validated_data)
        instance.lesson_id = lesson_id
        instance.save()
        return instance


class LessonSerializer(serializers.ModelSerializer):
    course = CourseGetSerializer(read_only=True)

    class Meta:
        model = Lesson
        fields = ['id', 'course', 'title', 'body', 'created_date']
        extra_fields = {
            "course": {"read_only": True},
        }


class LessonPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ['id', 'course', 'title', 'body', 'created_date']
        extra_fields = {
            "course": {"read_only": True},
        }

    def create(self, validated_data):
        course_id = self.context['course_id']
        instance = super().create(validated_data)
        instance.course_id = course_id
        instance.save()
        return instance


