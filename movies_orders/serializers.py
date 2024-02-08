from rest_framework import serializers

from movies_orders.models import MovieOrder


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    purchased_at = serializers.DateTimeField(read_only=True)
    title = serializers.SerializerMethodField()
    purchased_by = serializers.SerializerMethodField()

    def get_title(self, obj):
        return obj.movie.title

    def get_purchased_by(self, obj):
        return obj.user.email

    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)
