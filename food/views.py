from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from food.serializers import *


class FoodListCreateAPIView(ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodDetailsAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
