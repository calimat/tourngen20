from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Tournament(models.Model):
    def get_absolute_url(self):
        return reverse('view_tournament', args=[self.id])

class Team(models.Model):
    name = models.TextField(default='')
    tournament = models.ForeignKey(Tournament, default=None)
