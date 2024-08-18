# Файл хранит модели(таблици для баз данных) и логика отображения данных к етим моделям

# django
from django.db import models

# подключаем встроеную таблицу с пользователями
from django.contrib.auth.models import User

# my_project
from products.models import Product


# создаем свою модель
class SalesOrder(models.Model):
    # создаем колонки для нашей модели
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
    
    # отношение -- один ко многим --
    # on_delete указываем что будет происходить с ячейками указаного пользователя при его удалении
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # отношение -- многие ко многим --
    products = models.ManyToManyField(Product)
