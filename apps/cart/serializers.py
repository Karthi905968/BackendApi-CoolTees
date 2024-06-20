from rest_framework import serializers
from .models import CartModel

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartModel
        fileds = '__all__'
        deapth = 1

class CartAddSerializer(serializers.ModelSerializer):
    class Meta:
         model = CartModel
         fields = ['items', 'quantity', 'user']  #


