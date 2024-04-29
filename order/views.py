from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from my_cars.models import Car


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['customer']
    search_fields = ['date_created']
    def post(self, request):
        customer = request.user
        order = Order.objects.create(customer=customer)
        total_price = 0
        for item in request.data['items']:
            car = get_object_or_404(Car, pk=item['car_id'])
            quantity = item['quantity']
            price = car.price * quantity
            OrderItem.objects.create(order=order, car=car, quantity=quantity, price=price)
            total_price += price
        order.total_price = total_price
        order.save()
        return Response(OrderSerializer(order).data)
