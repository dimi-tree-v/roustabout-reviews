from releases.factories import ReleaseFactory
from reviews.models import ArticleReview, UserReview

from django.contrib.auth.models import User

class ArticleReviewFactory:
    @classmethod
    def create(
        cls,
        title="test_review_title",
        rating=2,
        author="test_user",
        release="test_song",
        body="test body",
    ):
        user = User.objects.get_or_create(username='testuser', password='12345')[0]
        release = ReleaseFactory.create()
        return ArticleReview.objects.get_or_create(
            title=title,
            rating=rating,
            author=user,
            release=release,
            body=body
        )[0]


class UserReviewFactory:
    @classmethod
    def create(
        cls,
        title="test_user_title",
        rating=2,
        author="test_user",
        release="test_song",
        body="test body",
    ):
        user = User.objects.get_or_create(username='testuser', password='12345')[0]
        release = ReleaseFactory.create()
        return UserReview.objects.get_or_create(
            title=title,
            rating=rating,
            author=user,
            release=release,
            body=body
        )[0]
