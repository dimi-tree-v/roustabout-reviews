from releases import serializers
from releases import models

from rest_framework import viewsets


class MemberViewSet(viewsets.ModelViewSet):
    queryset = models.Member.objects.all()
    serializer_class=  serializers.MemberSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = models.Genre.objects.all()
    serializer_class=  serializers.GenreSerializer


class ReleaseViewSet(viewsets.ModelViewSet):
    queryset = models.Release.objects.all()

    def get_serializer_class(self):
        if request.method == 'GET':
            return serializers.ReleaseDetailSerializer
        return serializers.ReleaseCreateSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = models.Artist.objects.all()
    serializer_class=  serializers.ArtistSerializer


class TrackViewSet(viewsets.ModelViewSet):
    queryset = models.Track.objects.all()
    serializer_class=  serializers.TrackSerializer
