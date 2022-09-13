from dataclasses import field
from rest_framework import  serializers
from .models import *


class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = "__all__"

class CategorySerielizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"