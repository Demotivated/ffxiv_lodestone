from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=100)
    lodestone_id = models.CharField(max_length=100)
    server = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    city_state = models.CharField(max_length=100)
    free_company = models.CharField(max_length=100)
    grand_company = models.CharField(max_length=100, default='')

    lvl_gladiator = models.IntegerField(default=0)
    lvl_pugilist = models.IntegerField(default=0)
    lvl_marauder = models.IntegerField(default=0)
    lvl_lancer = models.IntegerField(default=0)
    lvl_archer = models.IntegerField(default=0)
    lvl_rogue = models.IntegerField(default=0)

    lvl_conjurer = models.IntegerField(default=0)
    lvl_thaumaturge = models.IntegerField(default=0)
    lvl_arcanist = models.IntegerField(default=0)

    lvl_dark_night = models.IntegerField(default=0)
    lvl_machinist = models.IntegerField(default=0)
    lvl_astrologian = models.IntegerField(default=0)

    lvl_carpenter = models.IntegerField(default=0)
    lvl_blacksmith = models.IntegerField(default=0)
    lvl_armorer = models.IntegerField(default=0)
    lvl_goldsmith = models.IntegerField(default=0)
    lvl_leatherworker = models.IntegerField(default=0)
    lvl_weaver = models.IntegerField(default=0)
    lvl_alchemist = models.IntegerField(default=0)
    lvl_culinarian = models.IntegerField(default=0)
    lvl_miner = models.IntegerField(default=0)
    lvl_botanist = models.IntegerField(default=0)
    lvl_fisher = models.IntegerField(default=0)

    def as_dict(self):
        return {
            'name': self.name,
            'lodestone_id': self.lodestone_id,
            'server': self.server,
            'species': self.species,
            'city_state': self.city_state,
            'free_company': self.free_company,
            'grand_company': self.grand_company,
            'classes': {
                'gladiator': self.lvl_gladiator,
                'pugilist': self.lvl_pugilist,
                'marauder': self.lvl_marauder,
                'lancer': self.lvl_lancer,
                'archer': self.lvl_archer,
                'rogue': self.lvl_rogue,

                'conjurer': self.lvl_conjurer,
                'thaumaturge': self.lvl_thaumaturge,
                'arcanist': self.lvl_arcanist,

                'dark_night': self.lvl_dark_night,
                'machinist': self.lvl_machinist,
                'astrologian': self.lvl_astrologian,

                'carpenter': self.lvl_carpenter,
                'blacksmith': self.lvl_blacksmith,
                'armorer': self.lvl_armorer,
                'goldsmith': self.lvl_goldsmith,
                'leatherworker': self.lvl_leatherworker,
                'weaver': self.lvl_weaver,
                'alchemist': self.lvl_alchemist,
                'culinarian': self.lvl_culinarian,
                'miner': self.lvl_miner,
                'botanist': self.lvl_botanist,
                'fisher': self.lvl_fisher
            }
        }
