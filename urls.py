from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def welcome_view(request):
    return JsonResponse({"message": "Welcome to DelightAPI Authentication Service"})

urlpatterns = [
    path('', welcome_view),  # 👈 Root path
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
]
