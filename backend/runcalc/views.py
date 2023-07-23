from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Admin, User
from .serializers import AdminSerializer, UserSerializer

# Create your views here.
class AdminLoginView(APIView):
    def post(self, request):
        serializer = AdminSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        admin = serializer.validated_data
        refresh = RefreshToken.for_user(admin)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
        
class AdminViewSet(viewsets.ModelViewSet):
    # authentication_classes = TokenAuthentication,
    # permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    # authentication_classes = TokenAuthentication,
    # permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer