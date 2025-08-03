from rest_framework import serializers
from .models import CartItem
from cakes.serializers import CakeSerializer
from cakes.models import Cake

class CartItemSerializer(serializers.ModelSerializer):
    cake = CakeSerializer(read_only=True)
    cake_id = serializers.PrimaryKeyRelatedField(queryset=Cake.objects.all(), source='cake', write_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'cake', 'cake_id', 'quantity', 'custom_message']
