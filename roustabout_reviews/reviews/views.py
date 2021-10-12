from reviews import serializers, models

from rest_framework import viewsets

class UserReviewViewset(viewsets.ModelViewSet):
    queryset = models.UserReview.objects.all()
    serializer_class = serializers.UserReviewSerializer


class ArticleReviewViewset(viewsets.ModelViewSet):
    queryset = models.ArticleReview.objects.all()
    serializer_class = serializers.ArticleReviewSerializer

    def get_serializer_class(self):
        if self.request.method != 'GET':
            return serializers.ArticleReviewSerializer
        return serializers.ArticleReviewDetailSerializer
