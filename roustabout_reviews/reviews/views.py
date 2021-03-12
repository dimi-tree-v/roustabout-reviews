from reviews import serializers, models

from rest_framework import viewsets

class UserReviewViewset(viewsets.ModelViewSet):
    queryset = models.UserReview.objects.all()
    serializer_class = serializers.UserReviewSerializer


class ArticleReviewViewset(viewsets.ModelViewSet):
    queryset = models.ArticleReview.objects.all()
    serializer_class = serializers.ArticleReviewSerializer
