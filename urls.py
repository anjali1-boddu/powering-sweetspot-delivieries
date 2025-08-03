from django.urls import path
from .views import sales_analytics, top_cakes

urlpatterns = [
    path('sales/', sales_analytics),
    path('top-cakes/', top_cakes),
]
