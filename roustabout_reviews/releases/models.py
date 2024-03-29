from base.models import TimestampedIdModel
from base.utils import get_average

from django.db import models
from django.conf import settings
from django.utils.functional import cached_property

RELEASE_TYPES = [
    ('ALBUM', 'ALBUM'),
    ('EP', 'EP'),
    ('SINGLE', 'SINGLE'),
    ('LIVE ALBUM', 'LIVE ALBUM')
]


class Artist(TimestampedIdModel):
    name = models.CharField(max_length=80)
    date_formed = models.DateField(null=False)
    location_formed = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Member(TimestampedIdModel):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='members')
    year_joined = models.DateField(null=False)
    year_left = models.DateField(null=True)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

class Genre(TimestampedIdModel):
    name = models.CharField(max_length=35)
    description = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.name


class Release(TimestampedIdModel):
    title =  models.CharField(max_length=80)
    artists = models.ManyToManyField(Artist, related_name='releases')
    genre =  models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='releases')
    type = models.CharField(max_length=35, choices=RELEASE_TYPES)
    date_released = models.DateField()
    language = models.CharField(max_length=50, choices=settings.LANGUAGES)

    def __str__(self):
        return f'{self.title}'

    @cached_property
    def average_critic_rating(self):
        return get_average([
            article.rating
            for article
            in self.articles.all()
        ])


    @cached_property
    def average_user_rating(self):
        return get_average([
            user_review.rating
            for user_review
            in self.user_reviews.all()
        ])


class Track(TimestampedIdModel):
    title =  models.CharField(max_length=80)
    duration = models.DecimalField(decimal_places=2, max_digits=4)
    release = models.ForeignKey(Release, on_delete=models.CASCADE, related_name='tracks')

    def __str__(self):
        return f'{self.title}'
