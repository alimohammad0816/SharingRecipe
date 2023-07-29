from django.urls import path

from raw_material import views

urlpatterns = [
    path('createlist/', views.RawMaterialCreateListAPIView.as_view()),
    path('details/<int:pk>/', views.RawMaterialDetailsAPIView.as_view()),

]