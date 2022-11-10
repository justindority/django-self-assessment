"""View module for handling requests about artists"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Song, Artist, Genre
from django.db.models import Count, IntegerField

class ArtistView(ViewSet):
    """Level up artist view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single artist

        Returns:
            Response -- JSON serialized artist
        """

        artist = Artist.objects.get(pk=pk).annotate(song_count=Count('songs'))
        # artist = Artist.objects.annotate(song_count=Count('songs'))


        serializer = SingleArtistSerializer(artist)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all artists

        Returns:
            Response -- JSON serialized list of artists
        """

        artists = Artist.objects.all()

        serializer = AllArtistSerializer(artists, many=True) 
        return Response(serializer.data)


    def create(self, request):
        """Handle POST operations for artists

        Returns
            Response -- JSON serialized artist instance
        """

        artist = Artist.objects.create(
            name=request.data["name"],
            age=request.data["age"],
            bio=request.data["bio"]
        )
        serializer = AllArtistSerializer(artist)
        return Response(serializer.data)

class SongSerializer(serializers.ModelSerializer):
    """JSON serializer for songs
    """

    class Meta:
        model = Song
        fields = ('id', 'title', 'album')


class AllArtistSerializer(serializers.ModelSerializer):
    """JSON serializer for artists
    """

    songs = SongSerializer(many=True)

    class Meta:
        model = Artist
        fields = ('id', 'name', 'age', 'bio', 'songs')


class SingleArtistSerializer(serializers.ModelSerializer):

    song_count = serializers.IntegerField(default=None)

    class Meta:
        model = Artist
        fields = ('id', 'name', 'age', 'bio', 'song_count',)