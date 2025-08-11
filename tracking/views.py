from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def tracking_view(request, order_id):
    """
    GET: Get current tracking info
    PUT: Update tracking status/location
    """
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'GET':
        return Response({
            "order_id": order.id,
            "status": order.status,
            "current_location": order.current_location,
            "estimated_delivery": order.estimated_delivery
        })

    if request.method == 'PUT':
        status = request.data.get('status', order.status)
        location = request.data.get('current_location', order.current_location)
        order.status = status
        order.current_location = location
        order.save()

        return Response({
            "message": "Tracking updated successfully",
            "order_id": order.id,
            "status": order.status,
            "current_location": order.current_location
        })
