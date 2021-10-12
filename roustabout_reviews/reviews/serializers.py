from reviews import models
from rest_framework import serializers


class UserReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.UserReview
        fields = ['id', 'url', 'title', 'rating', 'author', 'release', 'body']


class ArticleReviewSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.ArticleReview
        fields = ['id', 'url', 'title', 'rating', 'author', 'release', 'body']


class ArticleReviewDetailSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.SerializerMethodField()
    release = serializers.SerializerMethodField()

    class Meta:
        model = models.ArticleReview
        fields = ['id', 'url', 'title', 'rating', 'author', 'release', 'body']

    def get_author(self, obj):
        return obj.author.username

    def get_release(self, obj):
        return obj.release.title
