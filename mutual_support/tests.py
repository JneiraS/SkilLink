import pytest
from django.contrib.auth.models import User

from .models import Profile


@pytest.mark.django_db
class TestProfileModel:
    @pytest.fixture
    def user(self, db):
        return User.objects.create_user(username='testuser', password='password')

    def test_profile_user_relation(self, user):
        profile = Profile.objects.create(user=user)
        assert profile.user == user

    def test_profile_bio_field(self):
        profile = Profile(bio="test")
        assert profile.bio == "test"
