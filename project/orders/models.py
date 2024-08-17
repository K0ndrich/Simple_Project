# Файл хранит модели(таблици для баз данных) и логика отображения данных к етим моделям

from django.db import models


# создаем свою модель
class SalesOrder(models.Model):
    # создаем колонки для нашей модели
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
