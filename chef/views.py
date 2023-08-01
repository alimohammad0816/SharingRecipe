from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from chef.serializers import *
from chef.models import Chef
from rest_framework.permissions import *


class ChefCreateListAPIView(ListCreateAPIView):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer


class ChefDetailsAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer



