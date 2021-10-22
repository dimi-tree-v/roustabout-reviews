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


class ReleaseCreateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Release
        fields = ['url', 'title', 'artists', 'genre', 'type', 'date_released', 'language']


class ReleaseDetailSerializer(serializers.HyperlinkedModelSerializer):
    artists = serializers.SerializerMethodField()
    genre = serializers.SerializerMethodField()
    articles = serializers.SerializerMethodField()

    class Meta:
        model = models.Release
        fields = ['id', 'url', 'title', 'artists', 'genre', 'type', 'date_released', 'language', 'articles', 'user_reviews']

    def get_artists(self, obj):
        return [artist.name for artist in obj.artists.all()]

    def get_genre(self, obj):
        return obj.genre.name

    def get_articles(self, obj):
        return [
            dict(
            id=article.id,
            title=article.title,
            author=article.author.username,
            rating=article.rating
            )
         for article in obj.articles.all()
         ]


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
