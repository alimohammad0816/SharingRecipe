from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chef/', include("chef.urls")),
    path('raw_material/', include("raw_material.urls")),
]
