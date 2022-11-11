"""View module for handling requests about songs"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Song, Artist, Genre
from tunaapi.views import AllArtistSerializer, SingleArtistSerializer

class SongView(ViewSet):
    """Level up games view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single song

        Returns:
            Response -- JSON serialized song
        """



        song = Song.objects.get(pk=pk)    
        serializer = SongSerializer(song)
        
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all songs

        Returns:
            Response -- JSON serialized list of songs
        """

        songs = Song.objects.all()

        if "genre" in request.query_params:
            songs = songs.filter(genre=request.query_params['genre'])
        elif "artist" in request.query_params:
            songs = songs.filter(artist=request.query_params['artist'])

        serializer = SongSerializer(songs, many=True) 
        return Response(serializer.data)


    def create(self, request):
        """Handle POST operations for songs

        Returns
            Response -- JSON serialized song instance
        """
        artist = Artist.objects.get(pk=request.data["artist"])
        serialized_artist = ArtistSerializer(artist)
        genre = Genre.objects.get(pk=request.data["genre"])
        serialized_genre = GenreSerializer(genre)



        song = Song.objects.create(
            title=request.data["title"],
            album=request.data["album"],
            length=request.data["length"],
            genre=genre,
            artist=artist        
            )
        serializer = SongSerializer(song)
        return Response(serializer.data)

class GenreSerializer(serializers.ModelSerializer):
    """JSON serializer for genres
    """
    class Meta:
        model = Genre
        fields = ('name',)

class ArtistSerializer(serializers.ModelSerializer):
    """JSON serializer for artits
    """
    class Meta:
        model = Artist
        fields = ('name',)

class SongSerializer(serializers.ModelSerializer):
    """JSON serializer for songs
    """

    genre = GenreSerializer(many=False)
    artist = ArtistSerializer(many=False)

    class Meta:
        model = Song
        fields = ('id', 'title', 'album', 'length', 'genre', 'artist')

        

