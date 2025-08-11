from django.urls import path
from .views import tracking_view

urlpatterns = [
    path('<int:order_id>/', tracking_view, name='tracking'),
]