from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import CartItem
from .serializers import CartItemSerializer
from cakes.models import Cake
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    serializer = CartItemSerializer(cart_items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    cake_id = request.data.get('cake_id')
    quantity = request.data.get('quantity', 1)
    message = request.data.get('message', '')

    try:
        cake = Cake.objects.get(id=cake_id)
    except Cake.DoesNotExist:
        return Response({'error': 'Cake not found'}, status=status.HTTP_404_NOT_FOUND)

    item, created = CartItem.objects.get_or_create(user=request.user, cake=cake)
    if not created:
        item.quantity += int(quantity)
    else:
        item.quantity = quantity
    item.message = message
    item.save()

    serializer = CartItemSerializer(item)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_from_cart(request, id):
    try:
        item = CartItem.objects.get(id=id, user=request.user)
        item.delete()
        return Response({'message': 'Item removed'}, status=status.HTTP_204_NO_CONTENT)
    except CartItem.DoesNotExist:
        return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_cart_item(request, id):
    try:
        item = CartItem.objects.get(id=id, user=request.user)
    except CartItem.DoesNotExist:
        return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

    item.quantity = request.data.get('quantity', item.quantity)
    item.message = request.data.get('message', item.message)
    item.save()

    serializer = CartItemSerializer(item)
    return Response(serializer.data)
from django.db import models
from authentication.models import User