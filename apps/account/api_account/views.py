from rest_framework import generics, status
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsOwnUserReadonly
from .serializers import RegisterSerializer, RegisterListSerializer, LoginSerializer, MyAccountSerializer, AccountUpdateSerializer
from ..models import Account


class AccountRegisterView(generics.GenericAPIView):
    # http://127.0.0.1:8000/api/account/register/
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        email = request.data.get('email')
        tokens = Account.objects.get(email=email).tokens
        user_data['tokens'] = tokens
        return Response({'success': True, 'data': user_data}, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    # http://127.0.0.1:8000/api/account/login/
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'tokens': serializer.data['tokens']}, status=status.HTTP_200_OK)


class MyAccount(generics.GenericAPIView):
    # http://127.0.0.1:8000/api/account/my/
    serializer_class = MyAccountSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = self.serializer_class(user)
        return Response({"success": True, 'data': serializer.data}, status=status.HTTP_200_OK)


class AccountRetrieveUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = AccountUpdateSerializer
    queryset = Account.objects.all()
    permission_classes = (IsOwnUserReadonly, IsAuthenticated)

    def get(self, request, *args, **kwargs):
        query = self.get_object()
        if query:
            serializer = self.get_serializer(query)
            return Response({"success": True, 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({"success": False, 'message': 'query did not exist'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({"success": False, 'message': 'credential is invalid'}, status=status.HTTP_404_NOT_FOUND)










