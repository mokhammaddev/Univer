from django.urls import path, include
from .views import PostViewSet, BodyUpdateDeleteAPIView, CommentListCreateAPIView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('post', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('post-rud/<int:pk>/', BodyUpdateDeleteAPIView.as_view()),
    path('<int:post_id>/comment/list-create/', CommentListCreateAPIView.as_view()),
]
