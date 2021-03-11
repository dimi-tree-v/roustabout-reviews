from releases import serializers
from releases import models

from rest_framework import viewsets

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = models.Artist.objects.all()
    serializer_class=  serializers.ArtistSerializer
