# Файл для управление панелью администратора и регистрации моделей(таблиц баз данных)

# django
from django.contrib import admin

# my_project
from orders.models import SalesOrder

admin.site.register(SalesOrder)
