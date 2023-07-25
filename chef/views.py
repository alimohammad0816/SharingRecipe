from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from chef.serializers import *


class ChefCreateListAPIView(ListCreateAPIView):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer


class ChefDetails(RetrieveUpdateDestroyAPIView):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer
