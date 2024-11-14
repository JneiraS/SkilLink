import pytest
from django.contrib.auth.models import User
from .models import Profile, UserCompetence, Creneau, Competence

@pytest.fixture
def user(db):
    """ Mock pour créer une instance d'utilisateur de test."""
    return User.objects.create_user(username='testuser', password='password')

@pytest.fixture
def profile(user):
    """ Mock pour créer une instance de Profile de test."""
    return Profile.objects.create(user=user)

@pytest.fixture
def competence():
    """ Mock pour créer une instance de Competence de test."""
    return Competence.objects.create(name='test_competence', category='test')

@pytest.mark.django_db
class TestProfileModel:
    def test_profile_user_relation(self, profile, user):
        assert profile.user == user

    def test_profile_bio_field(self, profile):
        profile.bio = "test"
        profile.save()
        assert profile.bio == "test"

@pytest.mark.django_db
class TestCompetenceModel:
    def test_competence_name_field(self, competence):
        assert competence.name == "test_competence"

    def test_competence_category_field(self, competence):
        assert competence.category == "test"

@pytest.mark.django_db
class TestCreneauModel:
    def test_creneau_creation(self, user, competence):
        creneau = Creneau.objects.create(
            date='2023-10-10',
            user=user,
            competence=competence,
            is_help_offered=True,
            description='Test description',
            is_reserved=False
        )
        assert creneau.date == '2023-10-10'
        assert creneau.user == user
        assert creneau.competence == competence
        assert creneau.is_help_offered is True
        assert creneau.description == 'Test description'
        assert creneau.is_reserved is False

@pytest.mark.django_db
class TestUserCompetenceModel:
    def test_usercompetence_creation(self, profile, competence):
        usercompetence = UserCompetence.objects.create(
            user=profile,
            competence=competence,
            is_offering=True
        )
        assert usercompetence.user == profile
        assert usercompetence.competence == competence
        assert usercompetence.is_offering is True
        assert str(usercompetence) == f"{profile} - {competence} (offre)"