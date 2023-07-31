from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from chef.serializers import *
from chef.serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from chef.serializers import RegisterSerializer
from rest_framework import generics
from chef.models import Chef


class ChefListAPIView(ListAPIView):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer


class ChefDetailsAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = Chef.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
