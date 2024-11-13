from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)


class Competence(models.Model):
    """
    Classe pour la gestion des compétences
    """
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=100, blank=True,
                                null=True)  # Optionnel, pour regrouper par catégorie

    def __str__(self):
        return self.name


class Creneau(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creneaux")
    competence = models.ForeignKey(Competence, on_delete=models.CASCADE)
    is_help_offered = models.BooleanField(default=True)  # True: offre d'aide, False: demande d'aide
    description = models.TextField(blank=True,
                                   null=True)
    is_reserved = models.BooleanField(default=False)


class UserCompetence(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    competence = models.ForeignKey(Competence, on_delete=models.CASCADE)
    is_offering = models.BooleanField(default=True)  # True: offre, False: recherche

    def __str__(self):
        return f"{self.user} - {self.competence} ({'offre' if self.is_offering else 'recherche'})"
