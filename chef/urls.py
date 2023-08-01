from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('createlist/', views.ChefCreateListAPIView.as_view()),
    path('details/<int:pk>/', views.ChefDetailsAPIView.as_view()),
    path('login/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]
