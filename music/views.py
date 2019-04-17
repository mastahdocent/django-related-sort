from rest_framework import generics

from music.models import Album
from music.serializers import AlbumSerializer

# Create your views here.

class AlbumsView(generics.ListAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
