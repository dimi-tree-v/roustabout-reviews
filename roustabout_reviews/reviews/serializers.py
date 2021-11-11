from reviews import models as review_models
from releases import models as release_models

from django.contrib.auth.models import User
from rest_framework import serializers


class UserReviewSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(), many=False, slug_field='username')

    class Meta:
        model = review_models.UserReview
        fields = ['id', 'url', 'title', 'rating', 'author', 'release', 'body']
        read_only_fields = ['id']


class ArticleReviewSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(), many=False, slug_field='username')
    release = serializers.SlugRelatedField(queryset=release_models.Release.objects.all(), many=False, slug_field='title')

    class Meta:
        model = review_models.ArticleReview
        fields = ['id', 'url', 'title', 'rating', 'author', 'artists', 'release', 'genre', 'body']
        read_only_fields = ['id', 'url', 'genre']
