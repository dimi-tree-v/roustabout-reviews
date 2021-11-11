from base.serializers import UserSerializer

from django.contrib.auth.models import User
from django.test import TestCase

class TestUserSerializer(TestCase):
    def setUp(self):
        self.test_user_data = dict(
            password = 'make_it_so',
            username = 'J.L. Picard',
            email = 'enterprise@uss.co.universe',
            is_staff = True,
            is_active = True,
        )

    def test_successful_create(self):
        test_user = UserSerializer().create(self.test_user_data)
        self.assertIsInstance(test_user, User)
