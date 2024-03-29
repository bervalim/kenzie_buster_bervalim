from rest_framework import serializers
from .models import RatingMovie
from .models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(
        max_length=10,
        allow_blank=True,
        default="",
    )
    rating = serializers.ChoiceField(
        choices=RatingMovie.choices,
        default=RatingMovie.G,
    )
    synopsis = serializers.CharField(
        allow_blank=True,
        default="",
    )
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, movie: Movie):
        return movie.user.email

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
