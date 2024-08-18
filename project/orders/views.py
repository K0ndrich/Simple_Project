# Файл хранит представления отображения страниц


# django
from django.shortcuts import render

# my_project
from orders.models import SalesOrder


def orders_page(request):
    return render(request, "index.html", {"orders": SalesOrder.objects.all()})
