from rest_framework import serializers
from .models import Order, OrderItem
from django.contrib.auth import get_user_model

User = get_user_model()


class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    items = serializers.ListField(child=serializers.PrimaryKeyRelatedField(queryset=OrderItem.objects.all(), required=True), required=True)
    ordered_date = serializers.DateField(format='%d %B %Y')

    class Meta:
        model = Order
        fields = ['owner', 'items', 'ordered_date']

 


class AddOrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ['product', 'date_added']

