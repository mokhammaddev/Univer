from django.urls import path
from .views import CategoryRUDApiView, CategoryListCreateApiView, TagRUDApiView, TagListCreateApiView, \
    ContactListCreateAPIView, ContactRUDAPIView, SubscribeListCreateAPIView, SubscribeRUDAPIView, \
    FAQListCreateAPIView, FAQRUDAPIView, AnswerListCreateAPIView, AnswerRUDQPIView

urlpatterns = [
    path('category/list-create/', CategoryListCreateApiView.as_view()),
    path('category/rud/<int:pk>', CategoryRUDApiView.as_view()),

    path('tag/list-create/', TagListCreateApiView.as_view()),
    path('tag/rud/<int:pk>', TagRUDApiView.as_view()),

    path('answer/list-create/', AnswerListCreateAPIView.as_view()),
    path('answer/rud/<int:pk>', AnswerRUDQPIView.as_view()),

    path('contact/list-create/', ContactListCreateAPIView.as_view()),
    path('contact/rud/<int:pk>', ContactRUDAPIView.as_view()),

    path('faq/list-create/', FAQListCreateAPIView.as_view()),
    path('faq/rud/<int:pk>', FAQRUDAPIView.as_view()),

    path('subscribe/list-create/', SubscribeListCreateAPIView.as_view()),
    path('subscribe/rud/<int:pk>', SubscribeRUDAPIView.as_view()),
]
