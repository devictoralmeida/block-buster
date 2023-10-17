from rest_framework import serializers
from movies.models import Movie, MovieRating


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(
        max_length=127,
        allow_blank=True,
        default="",
    )
    rating = serializers.ChoiceField(
        choices=MovieRating.choices, default=MovieRating.G
    )
    synopsis = serializers.CharField(
        max_length=127,
        allow_blank=True,
        default="",
    )
    added_by = serializers.EmailField(source="user.email", read_only=True)

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)
