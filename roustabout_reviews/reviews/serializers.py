from reviews import models
from rest_framework import serializers


class UserReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.UserReview
        fields = ['url', 'title', 'rating', 'author', 'release', 'body']


class ArticleReviewSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = models.ArticleReview
        fields = ['url', 'title', 'rating', 'author', 'release', 'body']

    def get_author(self, obj):
        return obj.author.username
