from reviews import models
from releases.serializers import ReleaseDetailSerializer
from rest_framework import serializers


class UserReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.UserReview
        fields = ['id', 'url', 'title', 'rating', 'author', 'release', 'body']
        read_only_fields = ['id']


class ArticleReviewCreateSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.ArticleReview
        fields = ['id', 'url', 'title', 'rating', 'author', 'release', 'body']
        read_only_fields = ['id']


class ArticleReviewDetailSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.SerializerMethodField()
    release = ReleaseDetailSerializer()

    class Meta:
        model = models.ArticleReview
        fields = ['id', 'url', 'title', 'rating', 'author', 'release', 'body']

    def get_author(self, obj):
        return obj.author.username
