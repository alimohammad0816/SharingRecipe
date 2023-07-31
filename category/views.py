from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from category.serializers import *


class CategoryCreateListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailsAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
