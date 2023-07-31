from django.urls import path
from . import views
from chef.views import RegisterView, MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('list/', views.ChefListAPIView.as_view()),
    path('details/<int:pk>/', views.ChefDetailsAPIView.as_view()),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),

]
