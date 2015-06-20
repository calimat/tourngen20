from django.db import models

# Create your models here.

class Tournament(models.Model):
    pass

class Team(models.Model):
    name = models.TextField(default='')
    tournament = models.ForeignKey(Tournament, default=None)
