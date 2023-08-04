from django.urls import path
from food import views

urlpatterns = [
    path('createlist/', views.FoodListCreateAPIView.as_view()),
    path('details/<int:pk>/', views.FoodDetailsAPIView.as_view()),

]