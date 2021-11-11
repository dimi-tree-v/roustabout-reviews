import datetime
from reviews.factories import ArticleReviewFactory, UserReviewFactory
from releases.factories import ArtistFactory, MemberFactory, GenreFactory, ReleaseFactory, TrackFactory
from django.test import TestCase


class TestArtist(TestCase):
    def setUp(self):
        self.artist = ArtistFactory.create()

    def test_str(self):
        self.assertEqual(str(self.artist), "dj-dimi")

class TestMember(TestCase):
    def setUp(self):
        self.member = MemberFactory.create()

    def test_str(self):
        self.assertEqual(str(self.member), "dimitri tree-v")

class TestGenre(TestCase):
    def setUp(self):
        self.genre = GenreFactory.create()

    def test_str(self):
        self.assertEqual(str(self.genre), "blues")

class TestRelease(TestCase):
    def setUp(self):
        self.release = ReleaseFactory.create()

    def test_str(self):
        self.assertEqual(str(self.release), "test_song")

    def test_average_critic_rating_no_ratings(self):
        self.assertEqual(self.release.average_critic_rating, None)

    def test_average_critic_rating(self):
        ArticleReviewFactory.create("test_article_1", 2)
        ArticleReviewFactory.create("test_article_2", 4)
        self.assertEqual(self.release.average_critic_rating, 3)

    def test_average_user_rating_no_ratings(self):
        self.assertEqual(self.release.average_user_rating, None)

    def test_average_user_rating_no_ratings(self):
        UserReviewFactory.create("test_user_review", 3)
        UserReviewFactory.create("test_user_review", 5)
        self.assertEqual(self.release.average_user_rating, 4)


class TestTrack(TestCase):
    def setUp(self):
        self.track = TrackFactory.create()

    def test_str(self):
        self.assertEquals(str(self.track), "the_test_blues")
