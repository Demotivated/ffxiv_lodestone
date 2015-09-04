from django.db import models


class Character(models.Model):
    lodestone_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    server = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    city_state = models.CharField(max_length=100)
    free_company = models.CharField(max_length=100)
    grand_company = models.CharField(max_length=100, default='')
