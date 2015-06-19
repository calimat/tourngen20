from django.db import models

# Create your models here.

class Tournament(models.Model):
    name = models.TextField(default='')
