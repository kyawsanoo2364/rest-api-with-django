from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User
from .serializer import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
