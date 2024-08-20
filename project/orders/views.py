# Файл хранит представления отображения страниц


# django
from django.shortcuts import render

# django_rest
from rest_framework.viewsets import ModelViewSet

# my_project
from orders.models import SalesOrder
from orders.serializers import OrderSerializer


def orders_page(request):
    return render(request, "index.html", {"orders": SalesOrder.objects.all()})


class OrderView(ModelViewSet):
    # queryset хранит елементы которые мы будем выводить в api
    queryset = SalesOrder.objects.all()
    serializer_class = OrderSerializer


def orders_app(request):
    return render(
        request,
        "main_app.html",
    )
