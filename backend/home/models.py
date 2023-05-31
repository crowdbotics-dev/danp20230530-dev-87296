from django.conf import settings
from django.db import models
class Luca(models.Model):
    'Generated Model'
    species = models.CharField(max_length=256,)
