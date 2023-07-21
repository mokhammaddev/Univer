from django.urls import path
from .views import AccountRegisterView, LoginView, MyAccount, AccountRetrieveUpdate
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', AccountRegisterView.as_view()),
    path('login/', LoginView.as_view()),

    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('my/', MyAccount.as_view()),
    path('retrieve-update/<int:pk>/', AccountRetrieveUpdate.as_view()),
]