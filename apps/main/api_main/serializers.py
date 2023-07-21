from ..models import Category, Tag, Answer, FAQ, Subscribe, Contact
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')

    def to_representation(self, instance):
        data = super(CategorySerializer, self).to_representation(instance)
        return data


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'title')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'question', 'answer')


class FAQSerializer(serializers.ModelSerializer):
    question = AnswerSerializer(read_only=True, many=True)

    class Meta:
        model = FAQ
        fields = ('id', 'question')


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = ('id', 'email')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'name', 'email', 'body', 'created_date')




