from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=100)
    lodestone_id = models.CharField(max_length=100, default='')
    server = models.CharField(max_length=100, default='')
    species = models.CharField(max_length=100, default='')
    city_state = models.CharField(max_length=100, default='')
    free_company = models.CharField(max_length=100, default='')
    grand_company = models.CharField(max_length=100, default='')

    def as_dict(self):

        class_dict = {}
        for c in [self.archer, self.lancer, self.marauder, self.pugilist, self.rogue, self.arcanist, self.conjurer, self.thaumaturge, self.astrologian, self.darknight, self.machinist, self.alchemist, self.armorer, self.blacksmith, self.carpenter, self.culinarian, self.gladiator, self.goldsmith, self.leatherworker, self.weaver, self.botanist, self.fisher, self.miner]:
            if not c:
                pass
            class_dict[c.__class__.__name__.lower()] = c.as_dict()

        return {
            'name': self.name,
            'lodestone_id': self.lodestone_id,
            'server': self.server,
            'species': self.species,
            'city_state': self.city_state,
            'free_company': self.free_company,
            'grand_company': self.grand_company,
            'classes': class_dict
        }


class Class(models.Model):
    character = models.OneToOneField(Character)
    level = models.IntegerField(default=0)

    def as_dict(self):
        return {
            'level': self.level
        }

    class Meta:
        abstract = True


class DiscipleOfWar(Class):
    class Meta:
        abstract = True


class DiscipleOfMagic(Class):
    class Meta:
        abstract = True


class DiscipleOfHand(Class):
    class Meta:
        abstract = True


class DiscipleOfLand(Class):
    class Meta:
        abstract = True


class Archer(DiscipleOfWar):
    pass


class Gladiator(DiscipleOfWar):
    pass


class Lancer(DiscipleOfWar):
    pass


class Marauder(DiscipleOfWar):
    pass


class Pugilist(DiscipleOfWar):
    pass


class Rogue(DiscipleOfWar):
    pass


class Arcanist(DiscipleOfMagic):
    pass


class Conjurer(DiscipleOfMagic):
    pass


class Thaumaturge(DiscipleOfMagic):
    pass


class Astrologian(DiscipleOfMagic):
    pass


class DarkNight(DiscipleOfWar):
    pass


class Machinist(DiscipleOfWar):
    pass


class Alchemist(DiscipleOfHand):
    pass


class Armorer(DiscipleOfHand):
    pass


class Blacksmith(DiscipleOfHand):
    pass


class Carpenter(DiscipleOfHand):
    pass


class Culinarian(DiscipleOfHand):
    pass


class Goldsmith(DiscipleOfHand):
    pass


class Leatherworker(DiscipleOfHand):
    pass


class Weaver(DiscipleOfHand):
    pass


class Botanist(DiscipleOfLand):
    pass


class Fisher(DiscipleOfLand):
    pass


class Miner(DiscipleOfLand):
    pass
