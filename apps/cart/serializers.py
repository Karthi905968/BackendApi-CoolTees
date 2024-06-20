from rest_framework import serializers
from .models import CartModel

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartModel
        fileds = ['items', 'quantity', 'user']
        deapth = 1

class CartAddSerializer(serializers.ModelSerializer):
    class Meta:
         model = CartModel
         fields = ['items', 'quantity', 'user']  #


