from releases import serializers
from releases import models

from django.core.exceptions import FieldError
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError


class MemberViewSet(viewsets.ModelViewSet):
    queryset = models.Member.objects.all()
    serializer_class = serializers.MemberSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = models.Genre.objects.all()
    serializer_class =  serializers.GenreSerializer


class ReleaseViewSet(viewsets.ModelViewSet):
    queryset = models.Release.objects.all()
    serializer_class = serializers.ReleaseSerializer


    def get_queryset(self):
        query_params = self.request.query_params.dict()
        if 'artists' in query_params.keys():
            query_params['artists__name'] = query_params.pop('artists')
        try:
            return self.queryset.filter(**query_params)
        except FieldError:
            raise ValidationError("Invalid query parameter", 400)


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = models.Artist.objects.all()
    serializer_class = serializers.ArtistSerializer

    def get_queryset(self):
        query_params = self.request.query_params.dict()
        return self.queryset.filter(**query_params)


class TrackViewSet(viewsets.ModelViewSet):
    queryset = models.Track.objects.all()
    serializer_class = serializers.TrackSerializer
