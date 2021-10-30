from releases import models
from reviews.serializers import ArticleReviewSerializer, UserReviewSerializer

from rest_framework import serializers


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Member
        fields = ['url', 'first_name', 'last_name', 'artist', 'role', 'year_joined', 'year_left']


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Genre
        fields = ['url', 'name', 'description']


class ReleaseCreateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Release
        fields = ['url', 'title', 'artists', 'genre', 'type', 'date_released', 'language']


class ReleaseDetailSerializer(serializers.HyperlinkedModelSerializer):
    artists = serializers.SlugRelatedField(read_only=True, many=True, slug_field='name')
    genre = serializers.StringRelatedField(read_only=True, many=False)
    articles = ArticleReviewSerializer(read_only=True, many=True)
    user_reviews = UserReviewSerializer(read_only=True, many=True)

    class Meta:
        model = models.Release
        fields = ['id', 'url', 'title', 'artists', 'genre', 'type', 'date_released', 'language', 'articles', 'user_reviews']


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    members = serializers.SlugRelatedField(many=True, read_only=True, slug_field='full_name')
    releases = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')

    class Meta:
        model = models.Artist
        fields = ['url', 'name', 'date_formed', 'location_formed', 'members', 'releases']


class TrackSerializer(serializers.HyperlinkedModelSerializer):
    release = ReleaseCreateSerializer(many=False, required=True)

    class Meta:
        model = models.Track
        fields = ['url', 'title', 'duration', 'release']
