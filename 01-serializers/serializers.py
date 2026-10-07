from django.db import models
from rest_framework import serializers

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    published = models.DateField()


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author", "price", "published"]

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "The value must be greater than 0"
            )
        return value

    def validate(self, data):
        if "dummy" in data["title"].lower():
            raise serializers.ValidationError(
                "Title can't contain dummy."
            )
        return data