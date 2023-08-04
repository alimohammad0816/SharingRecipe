from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from raw_material.serializers import *
from rest_framework.permissions import *


class RawMaterialCreateListAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialSerializer


class RawMaterialDetailsAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialSerializer
