from django.urls import path

from category import views

urlpatterns = [
    path('createlist/', views.CategoryCreateListAPIView.as_view()),
    path('details/<int:pk>/', views.CategoryDetailsAPIView.as_view()),

]