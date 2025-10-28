
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ["id", "name", "price", "tags"]

    def get_tags(self, obj):
        tags = obj.tags or []
        return sorted([str(t) for t in tags], key=lambda x: x.lower())

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("El precio no puede ser negativo.")
        return value
