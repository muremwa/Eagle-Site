import time

from django.test import TestCase
from django.contrib.auth.models import User

from .models import EagleProfile


class EagleModelsTestCase(TestCase):
    def test_eagle_profile(self):
        user = User.objects.create(
            username='muremwa',
            password='pass@123'
        )
        user_2 = User.objects.create(
            username='muremwa_2',
            password='pass@1234',
            is_superuser=True
        )
        profile = EagleProfile.objects.get(pk=1)
        self.assertEqual(profile.user, user_2)
