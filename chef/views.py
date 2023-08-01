from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from chef.serializers import *
from chef.models import Chef


class ChefCreateListAPIView(ListCreateAPIView):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer


class ChefDetailsAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer



