from django.urls import path
from .views import blog, detail


urlpatterns = [
    path('blog/', blog, name='blog'),
    path('detail/<int:pk>/', detail, name='detail'),
]
