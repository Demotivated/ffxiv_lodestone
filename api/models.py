from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=100)
    lodestone_id = models.CharField(max_length=100)
    server = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    city_state = models.CharField(max_length=100)
    free_company = models.CharField(max_length=100)
    grand_company = models.CharField(max_length=100, default='')

    def as_dict(self):
        return {
            'name': self.name,
            'lodestone_id': self.lodestone_id,
            'server': self.server,
            'species': self.species,
            'city_state': self.city_state,
            'free_company': self.free_company,
            'grand_company': self.grand_company
        }
