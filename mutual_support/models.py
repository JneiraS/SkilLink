from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()


class Competence(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=100, blank=True,
                                null=True)  # Optionnel, pour regrouper par catégorie

    def __str__(self):
        return self.name
