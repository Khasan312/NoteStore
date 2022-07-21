from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import AddOrderItemSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Order


class AddItem(CreateAPIView):
    serializer_class = AddOrderItemSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        new_order_item = serializer.save()
        new_order = Order.objects.create()
        new_order.items.add(new_order_item)


class OrderView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer