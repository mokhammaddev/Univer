from apps.main.models import Category, Tag
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from .serializers import PostDetailSerializer, PostSerializer, BodySerializer, CommentSerializer
from ..models import Post, Body, Comment


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'put', 'patch']:
            return PostSerializer
        return PostDetailSerializer


class BodyUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Body.objects.all()
    serializer_class = BodySerializer


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['post_id'] = self.kwargs.get('post_id')
        return ctx

    def get_queryset(self):
        qs = super().get_queryset()
        post_id = self.kwargs.get('post_id')
        qs = qs.filter(post_id=post_id)
        return qs
