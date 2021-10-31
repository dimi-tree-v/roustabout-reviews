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


class ReleaseSerializer(serializers.HyperlinkedModelSerializer):
    artists = serializers.SlugRelatedField(read_only=True, many=True, slug_field='name')
    genre = serializers.SlugRelatedField(read_only=True, many=False, slug_field='name')
    articles = ArticleReviewSerializer(read_only=True, many=True)
    user_reviews = UserReviewSerializer(read_only=True, many=True)
    average_critic_rating = serializers.CharField(read_only=True)
    average_user_rating = serializers.CharField(read_only=True)

    class Meta:
        model = models.Release
        fields = [
            'id', 'url', 'title', 'artists', 'genre', 'type', 'average_critic_rating', 'average_user_rating',
            'date_released', 'language', 'articles', 'user_reviews',
        ]
        read_only_fields = [
            'id', 'average_critic_rating', 'average_user_rating', 'articles', 'user_reviews',
        ]


class ArtistReleaseSerializer(serializers.HyperlinkedModelSerializer):
    genre = serializers.SlugRelatedField(read_only=True, many=False, slug_field='name')
    average_critic_rating = serializers.CharField(read_only=True)
    average_user_rating = serializers.CharField(read_only=True)

    class Meta:
        model = models.Release
        fields = [
            'id', 'title', 'genre', 'type', 'average_critic_rating', 'average_user_rating',
            'date_released',
        ]
        read_only_fields = fields


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    members = serializers.SlugRelatedField(many=True, read_only=True, slug_field='full_name')
    releases = ArtistReleaseSerializer(many=True, read_only=True)

    class Meta:
        model = models.Artist
        fields = ['url', 'name', 'date_formed', 'location_formed', 'members', 'releases']


class TrackSerializer(serializers.HyperlinkedModelSerializer):
    release = ReleaseSerializer(many=False, required=True)

    class Meta:
        model = models.Track
        fields = ['url', 'title', 'duration', 'release']
