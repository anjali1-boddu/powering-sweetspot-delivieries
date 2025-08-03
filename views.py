from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from orders.models import Order
from cakes.models import Cake
from collections import Counter

@api_view(['GET'])
@permission_classes([IsAdminUser])
def sales_analytics(request):
    orders = Order.objects.all()
    total_orders = orders.count()
    total_revenue = sum(order.total_price for order in orders)

    return Response({
        'total_orders': total_orders,
        'total_revenue': total_revenue
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def top_cakes(request):
    orders = Order.objects.all()
    cake_counter = Counter()

    for order in orders:
        for item in order.items.all():
            cake_counter[item.cake.name] += item.quantity

    top_cakes = cake_counter.most_common(5)

    return Response({
        'top_cakes': [{'name': name, 'quantity_sold': qty} for name, qty in top_cakes]
    })
