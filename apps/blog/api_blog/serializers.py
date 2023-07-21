from rest_framework import serializers
from apps.main.api_main.serializers import CategorySerializer, TagSerializer
from ..models import Post, Body, Comment
from apps.main.models import Category, Tag
from apps.account.api_account.serializers import MyAccountSerializer


class BodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields = ('id', 'body', 'is_script')
        extra_kwargs = {
            "post": {"required": False}
        }


class PostDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)
    author = MyAccountSerializer(read_only=True)
    post_body = BodySerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'category', 'image', 'post_body', 'tags', 'created_date', 'modified_date')


class PostSerializer(serializers.ModelSerializer):
    post_body = BodySerializer(required=False, many=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'post_body', 'category', 'image', 'tags', 'created_date', 'modified_date')
        extra_kwargs = {
            "author": {"read_only": True},
            "image": {"required": False}
        }

    def create(self, validated_data):
        post_body = validated_data.pop('post_body', None)
        tags = validated_data.pop('tags', None)
        request = self.context['request']
        instance = Post.objects.create(author_id=request.user.id, **validated_data)
        if tags:
            for tag in tags:
                instance.tags.add(tag)
        if post_body:
            for body in post_body:
                Body.objects.create(post_id=instance.id, body=body['body'], is_script=body['is_script'])
        return instance


class MiniCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'body', 'created_date', 'top_level_comment_id')


class CommentSerializer(serializers.ModelSerializer):
    author = MyAccountSerializer(read_only=True)
    children = serializers.SerializerMethodField(read_only=True)

    def get_children(self, obj):
        children = Comment.objects.filter(parent_comment_id=obj.id)
        serializer = MiniCommentSerializer(children, many=True)
        return serializer.data

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'body', 'created_date', 'children', 'top_level_comment_id')
        extra_fields = {
            "author": {"read_only": True},
            "top_level_comment_id": {"read_only": True},
            "post": {"read_only": True},
        }

    def create(self, validated_data):
        request = self.context['request']
        post_id = self.context['post_id']
        user_id = request.user.id
        instance = Comment.objects.create(post_id=post_id, user_id=user_id, **validated_data)
        return instance



