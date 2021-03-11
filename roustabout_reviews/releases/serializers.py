from releases.models import Artist, Member
from rest_framework import serializers

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ['url', 'name', 'date_formed', 'location_formed']

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ['url', 'name', 'date_formed', 'location_formed']
