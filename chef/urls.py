from django.urls import path
from . import views

urlpatterns = [
    path('createlist/', views.ChefCreateListAPIView.as_view()),
    path('details/<int:pk>/', views.ChefDetailsAPIView.as_view()),

]