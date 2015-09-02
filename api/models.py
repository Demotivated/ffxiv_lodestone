from django.db import models


class Character(models.Model):
    lodestone_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    server = models.CharField(max_length=20)
    species = models.CharField(max_length=20)
    city_state = models.CharField(max_length=20)
    free_company = models.CharField(max_length=100)
