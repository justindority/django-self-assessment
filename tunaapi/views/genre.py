from rest_framework import serializers
from tunaapi.models import Genre

class GenreSerializer(serializers.ModelSerializer):
    """JSON serializer for genres
    """
    class Meta:
        model = Genre
        fields = ('id', 'name')