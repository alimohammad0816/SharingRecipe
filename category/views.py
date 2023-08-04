from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from category.serializers import *
from rest_framework.permissions import *


class CategoryCreateListAPIView(ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailsAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
