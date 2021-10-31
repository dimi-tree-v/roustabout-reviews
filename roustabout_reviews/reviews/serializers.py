from reviews import models

from django.contrib.auth.models import User
from rest_framework import serializers


class UserReviewSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(), many=False, slug_field='username')

    class Meta:
        model = models.UserReview
        fields = ['id', 'url', 'title', 'rating', 'author', 'release', 'body']
        read_only_fields = ['id']


class ArticleReviewSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, many=False, slug_field='username')
    release = serializers.SlugRelatedField(read_only=True, many=False, slug_field='title')

    class Meta:
        model = models.ArticleReview
        fields = ['id', 'url', 'title', 'rating', 'author', 'artists', 'release', 'genre', 'body']
        read_only_fields = ['id', 'url', 'author', 'release', 'genre']
