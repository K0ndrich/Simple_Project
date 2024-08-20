
# django

# django_rest
from rest_framework.serializers import ModelSerializer

# my_project
from orders.models import SalesOrder


class OrderSerializer(ModelSerializer):

    class Meta:
        model = SalesOrder
        fields = ["amount", "description"]
