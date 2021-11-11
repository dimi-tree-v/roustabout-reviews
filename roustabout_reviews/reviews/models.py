from base.models import TimestampedIdModel
from releases.models import Release

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.functional import cached_property

class Review(TimestampedIdModel):
    title = models.CharField(max_length=80)
    rating = models.DecimalField(decimal_places=1, max_digits=2, validators=[MaxValueValidator(5), MinValueValidator(0)])

    class Meta:
        abstract = True

class UserReview(Review):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reviews')
    release = models.ForeignKey(Release, on_delete=models.CASCADE, related_name='user_reviews')
    body = models.TextField(max_length=2000)

class ArticleReview(Review):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    release = models.ForeignKey(Release, on_delete=models.CASCADE, related_name='articles')
    body = models.TextField(max_length=6000)

    @cached_property
    def artists(self):
        return [str(artist) for artist in self.release.artists.all()]

    @cached_property
    def genre(self):
        return self.release.genre.name
