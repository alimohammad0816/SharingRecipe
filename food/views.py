from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from food.serializers import *
from rest_framework.permissions import *


def remove_dict_none_value(data: dict) -> dict:
    if data:
        return {k: v for k, v in data.items() if v is not None}


class FoodListCreateAPIView(ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def get_request_data_filter(self):
        name = self.request.query_params.get('name')
        ranking = self.request.query_params.get('ranking')
        foods_category = self.request.query_params.get('foods_category')
        chefs_of_food = self.request.query_params.get('chefs_of_food')

        dic_output = {'name': name,
                      'ranking': ranking,
                      'foods_category': foods_category,
                      'chefs_of_food': chefs_of_food,
                      }
        return dic_output

    def get_queryset(self):
        _input = self.get_request_data_filter()
        _filter = remove_dict_none_value(_input)

        return Food.objects.all().filter(**_filter)


class FoodDetailsAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
