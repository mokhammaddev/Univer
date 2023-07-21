from django.urls import path, include

app_name = 'main'

urlpatterns = [
    path('', include('apps.main.v1.urls')),
]
