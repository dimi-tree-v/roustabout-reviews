import datetime
from releases.models import Artist, Member, Genre, Release


class ArtistFactory:
    @classmethod
    def create(
        cls,
        name='dj-dimi',
        date_formed=datetime.date(2010, 1, 1),
        location_formed='tree'
    ):
        return Artist.objects.get_or_create(
            name=name,
            date_formed=date_formed,
            location_formed=location_formed
        )[0]


class MemberFactory:
    @classmethod
    def create(
        cls,
        artist_name='dj-dimi',
        first_name='dimitri',
        last_name='tree-v',
        year_joined=datetime.date(2010, 1, 1),
        year_left=datetime.date(2010, 2, 1),
        role='guitarist'
     ):
        artist = ArtistFactory.create(name=artist_name)
        return Member.objects.get_or_create(
            first_name=first_name,
            last_name=last_name,
            artist=artist,
            year_joined=year_joined,
            year_left=year_left,
            role=role
        )[0]


class GenreFactory:
    @classmethod
    def create(
        cls,
        name='blues',
        description='Genre originating from...'
    ):
        return Genre.objects.get_or_create(
            name=name,
            description=description
        )[0]

class ReleaseFactory:
    @classmethod
    def create(
        cls,
        title='test_song',
        artist_names=['dj-dimi'],
        genre_name='blues',
        type='SINGLE',
        date_released=datetime.date(2010, 1, 1),
        language='Greek'
    ):
        artists = [ArtistFactory.create(name) for name in artist_names]
        genre = GenreFactory.create(name=genre_name)
        release = Release.objects.get_or_create(
            title=title,
            genre=genre,
            type=type,
            date_released=date_released,
            language=language
        )[0]
        ReleaseFactory._assign_artist(artists, release)
        return release

    @classmethod
    def _assign_artist(self, artists, release):
        for artist in artists:
            artist.release=release
            artist.save()

class TrackFactory:
    @classmethod
    def create(
        cls,
        title='the_test_blues',
        duration='Genre originating from...',
        release='test_song'
    ):
        release = ReleaseFactory.create(title=title)
        return Genre.objects.get_or_create(
            title=title,
            duration=duration,
            release=release
        )[0]
