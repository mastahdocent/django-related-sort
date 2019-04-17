from rest_framework import serializers

from music.models import Album, Track


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id', 'title']


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'title', 'artist', 'order', 'tracks']

    tracks = serializers.SerializerMethodField()

    def get_tracks(self, instance):
        return TrackSerializer(instance.get_tracks(), many=True).data
