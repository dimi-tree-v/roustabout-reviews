from releases import models
from rest_framework import serializers


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Member
        fields = ['url', 'first_name', 'last_name', 'artist', 'role', 'year_joined', 'year_left']


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Genre
        fields = ['url', 'name', 'description']


class ReleaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Release
        fields = ['url', 'title', 'artists', 'genre', 'type', 'date_released', 'language']


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    members = serializers.SlugRelatedField(many=True, read_only=True, slug_field='full_name')
    releases = serializers.SlugRelatedField(many=True, read_only=True, slug_field='display_name')

    class Meta:
        model = models.Artist
        fields = ['url', 'name', 'date_formed', 'location_formed', 'members', 'releases']


class TrackSerializer(serializers.HyperlinkedModelSerializer):
    release = ReleaseSerializer(many=False, required=True)

    class Meta:
        model = models.Track
        fields = ['url', 'title', 'duration', 'release']
