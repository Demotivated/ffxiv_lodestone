import logging

from django.db import models

from .constants import JOBS, JOBS_CHOICES


class Character(models.Model):
    """
    A single character's basic info and refers to all their known jobs.
    """
    name = models.CharField(max_length=100)
    """
    :type: String
    """

    lodestone_id = models.CharField(max_length=100, default='', unique=True)
    """
    Unique for each item.

    Used to scrape the item's info from Lodestone, see below.

    .. image:: ../../images/character_lodestone_id.PNG

    :type: String
    """

    server = models.CharField(max_length=100, default='')
    """
    :type: String
    """

    species = models.CharField(max_length=100, default='')
    """
    :type: String
    """

    gender = models.CharField(max_length=20, default='')
    """
    :type: String
    """

    city_state = models.CharField(max_length=100, default='')
    """
    :type: String
    """

    free_company_name = models.CharField(max_length=100, default='')
    """
    :type: String
    """

    free_company_id = models.CharField(max_length=100, default='')
    """
    :type: String
    """

    grand_company_name = models.CharField(max_length=100, default='')
    """
    :type: String
    """

    grand_company_rank = models.CharField(max_length=100, default='')
    """
    :type: String
    """

    lvl_archer = models.IntegerField(default=0)
    lvl_lancer = models.IntegerField(default=0)
    lvl_marauder = models.IntegerField(default=0)
    lvl_pugilist = models.IntegerField(default=0)
    lvl_rogue = models.IntegerField(default=0)
    lvl_arcanist = models.IntegerField(default=0)
    lvl_conjurer = models.IntegerField(default=0)
    lvl_thaumaturge = models.IntegerField(default=0)
    lvl_astrologian = models.IntegerField(default=0)
    lvl_darknight = models.IntegerField(default=0)
    lvl_machinist = models.IntegerField(default=0)
    lvl_alchemist = models.IntegerField(default=0)
    lvl_armorer = models.IntegerField(default=0)
    lvl_blacksmith = models.IntegerField(default=0)
    lvl_carpenter = models.IntegerField(default=0)
    lvl_culinarian = models.IntegerField(default=0)
    lvl_gladiator = models.IntegerField(default=0)
    lvl_goldsmith = models.IntegerField(default=0)
    lvl_leatherworker = models.IntegerField(default=0)
    lvl_weaver = models.IntegerField(default=0)
    lvl_botanist = models.IntegerField(default=0)
    lvl_fisher = models.IntegerField(default=0)
    lvl_miner = models.IntegerField(default=0)

    @property
    def as_dict(self):
        """
        :return: Dictionary of the the class' values for easier JSON serialization

        :rtype: Dictionary
        """
        jobs = list(map(lambda x: x.as_dict, list(self.job_set.all()))) if len(self.job_set.all()) > 0 else []

        return {
            'name': self.name,
            'lodestone_id': self.lodestone_id,
            'server': self.server,
            'species': self.species,
            'gender': self.gender,
            'city_state': self.city_state,
            'free_company': {
                'name': self.free_company_name,
                'lodestone_id': self.free_company_id
            },
            'grand_company': {
                'name': self.grand_company_name,
                'rank': self.grand_company_rank
            },
            'jobs': jobs,
            'classes': {
                "armorer": {
                    "level": self.lvl_armorer
                },
                "alchemist": {
                    "level": self.lvl_alchemist
                },
                "leatherworker": {
                    "level": self.lvl_leatherworker
                },
                "pugilist": {
                    "level": self.lvl_pugilist
                },
                "carpenter": {
                    "level": self.lvl_carpenter
                },
                "culinarian": {
                    "level": self.lvl_culinarian
                },
                "arcanist": {
                    "level": self.lvl_arcanist
                },
                "fisher": {
                    "level": self.lvl_fisher
                },
                "machinist": {
                    "level": self.lvl_machinist
                },
                "conjurer": {
                    "level": self.lvl_conjurer
                },
                "blacksmith": {
                    "level": self.lvl_blacksmith
                },
                "astrologian": {
                    "level": self.lvl_astrologian
                },
                "thaumaturge": {
                    "level": self.lvl_thaumaturge
                },
                "gladiator": {
                    "level": self.lvl_gladiator
                },
                "miner": {
                    "level": self.lvl_miner
                },
                "lancer": {
                    "level": self.lvl_lancer
                },
                "rogue": {
                    "level": self.lvl_rogue
                },
                "marauder": {
                    "level": self.lvl_marauder
                },
                "botanist": {
                    "level": self.lvl_botanist
                },
                "weaver": {
                    "level": self.lvl_weaver
                },
                "archer": {
                    "level": self.lvl_archer
                },
                "darknight": {
                    "level": self.lvl_darknight
                },
                "goldsmith": {
                    "level": self.lvl_goldsmith
                }
            }
        }

    def __str__(self):
        return '{name}'.format(
            name=self.name
        )

    def __repr__(self):
        return '<Character name={name} id={id}>'.format(
            name=self.name,
            id=self.lodestone_id
        )


class Item(models.Model):
    """
    A weapon, armor, shield, accessory, or soul stone.

    Generated and added to DB by :func:`api.scrapers.character.scrape_item_by_id`.

    Do not initialize this yourself.
    """
    lodestone_id = models.CharField(max_length=200, unique=True)
    """

    Unique for each item.

    Used to scrape the item's info from Lodestone, see below.

    .. image:: ../../images/item_lodestone_id.PNG

    :type: String
    """

    name = models.CharField(max_length=200)
    """
    :type: String
    """

    item_type = models.CharField(max_length=100, default='Body')
    """
    Examples:

    - Body
    - Soul Crystal
    - Necklace
    - Two-handed Conjurer's Arm

    :type: String
    """

    item_level = models.IntegerField(default=0)
    """
    iLevel

    :type: Int
    """

    damage = models.IntegerField(default=0)
    auto_attack = models.FloatField(default=0)
    delay = models.FloatField(default=0)

    defense = models.IntegerField(default=0)
    magic_defense = models.IntegerField(default=0)

    block_strength = models.IntegerField(default=0)
    block_rate = models.IntegerField(default=0)

    vitality = models.IntegerField(default=0)
    mind = models.IntegerField(default=0)
    determination = models.IntegerField(default=0)
    spell_speed = models.IntegerField(default=0)
    accuracy = models.IntegerField(default=0)
    critical_hit_rate = models.IntegerField(default=0)
    piety = models.IntegerField(default=0)

    @property
    def as_dict(self):
        """

        ::

            {
                "lodestone_id": "fa0a11eb218",
                "type": "Head",
                "name": "Platinum Circlet of Healing",
                "stats": {
                    "mind": 24,
                    "determination": 0,
                    "armor_stats": {
                        "magic_defense": 66,
                        "defense": 38
                    },
                    "accuracy": 5,
                    "shield_stats": {
                        "block_strength": 0,
                        "block_rate": 0
                    },
                    "piety": 13,
                    "critical_hit_rate": 25,
                    "weapon_stats": {
                        "delay": 0.0,
                        "damage": 0,
                        "auto_attack": 0.0
                    },
                    "spell_speed": 0,
                    "vitality": 25
                },
                "ilevel": 110
            }

        :return: Dictionary of the item's properties. Very closely mirrors the JSON representation
        """
        try:
            return {
                'lodestone_id': self.lodestone_id,
                'name': self.name,
                'ilevel': self.item_level,
                'type': self.item_type,
                'stats': {
                    'weapon_stats': {
                        'damage': self.damage,
                        'auto_attack': self.auto_attack,
                        'delay': self.delay
                    },
                    'armor_stats': {
                        'defense': self.defense,
                        'magic_defense': self.magic_defense
                    },
                    'shield_stats': {
                        'block_strength': self.block_strength,
                        'block_rate': self.block_rate
                    },
                    'vitality': self.vitality,
                    'mind': self.mind,
                    'determination': self.determination,
                    'spell_speed': self.spell_speed,
                    'accuracy': self.accuracy,
                    'critical_hit_rate': self.critical_hit_rate,
                    'piety': self.piety
                }
            }
        except TypeError:
            logging.error('Unable to parse to dict {}'.format(self.__repr__()), exc_info=True)

    def __repr__(self):
        return '<Item name={name} id={lodestone_id} type={type}>'.format(
            name=self.name,
            lodestone_id=self.lodestone_id,
            type=self.item_type
        )

    def __str__(self):
        return '{name}'.format(
            name=self.name
        )


class Job(models.Model):
    """
    A single job for any given :class:`api.models.Character` and all its items / stats

    Jobs are a *superset* of classes. For example, all of the following are jobs for simplicity

    * Archer
    * Bard
    * Blacksmith
    * Machinist
    """
    character = models.ForeignKey(Character)
    job = models.CharField(max_length=25, choices=JOBS_CHOICES)
    items = models.ManyToManyField(Item)

    hp = models.IntegerField(default=0)
    mp = models.IntegerField(default=0)
    tp = models.IntegerField(default=0)

    strength = models.IntegerField(default=0)
    dexterity = models.IntegerField(default=0)
    vitality = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    mind = models.IntegerField(default=0)
    piety = models.IntegerField(default=0)

    fire = models.IntegerField(default=0)
    ice = models.IntegerField(default=0)
    wind = models.IntegerField(default=0)
    earth = models.IntegerField(default=0)
    lightning = models.IntegerField(default=0)
    water = models.IntegerField(default=0)

    accuracy = models.IntegerField(default=0)
    crit_rate = models.IntegerField(default=0)
    determination = models.IntegerField(default=0)

    defense = models.IntegerField(default=0)
    parry = models.IntegerField(default=0)
    magic_defense = models.IntegerField(default=0)

    attack_power = models.IntegerField(default=0)
    skill_speed = models.IntegerField(default=0)

    attack_magic_potency = models.IntegerField(default=0)
    healing_magic_potency = models.IntegerField(default=0)
    spell_speed = models.IntegerField(default=0)

    slow_resist = models.IntegerField(default=0)
    silence_resist = models.IntegerField(default=0)
    blind_resist = models.IntegerField(default=0)
    poison_resist = models.IntegerField(default=0)
    stun_resist = models.IntegerField(default=0)
    sleep_resist = models.IntegerField(default=0)
    bind_resist = models.IntegerField(default=0)
    heavy_resist = models.IntegerField(default=0)

    slashing_resist = models.IntegerField(default=0)
    piercing_resist = models.IntegerField(default=0)
    blunt_resist = models.IntegerField(default=0)

    @property
    def level(self):
        """


        :return: The job's level derived from the character's class levels
        """
        if self.job == JOBS.MARAUDER.name:
            return self.character.lvl_marauder
        elif self.job == JOBS.GLADIATOR.name:
            return self.character.lvl_gladiator
        elif self.job == JOBS.PUGILIST.name:
            return self.character.lvl_pugilist
        elif self.job == JOBS.LANCER.name:
            return self.character.lvl_lancer
        elif self.job == JOBS.ARCHER.name:
            return self.character.lvl_archer
        elif self.job == JOBS.ROGUE.name:
            return self.character.lvl_rogue
        elif self.job == JOBS.CONJURER.name:
            return self.character.lvl_conjurer
        elif self.job == JOBS.THAUMATURGE.name:
            return self.character.lvl_thaumaturge
        elif self.job == JOBS.ARCANIST.name:
            return self.character.lvl_arcanist

        elif self.job == JOBS.CARPENTER.name:
            return self.character.lvl_carpenter
        elif self.job == JOBS.BLACKSMITH.name:
            return self.character.lvl_blacksmith
        elif self.job == JOBS.ARMORER.name:
            return self.character.lvl_armorer
        elif self.job == JOBS.GOLDSMITH.name:
            return self.character.lvl_goldsmith
        elif self.job == JOBS.LEATHERWORKER.name:
            return self.character.lvl_leatherworker
        elif self.job == JOBS.WEAVER.name:
            return self.character.lvl_weaver
        elif self.job == JOBS.ALCHEMIST.name:
            return self.character.lvl_alchemist
        elif self.job == JOBS.CULINARIAN.name:
            return self.character.lvl_culinarian
        elif self.job == JOBS.BOTANIST.name:
            return self.character.lvl_botanist
        elif self.job == JOBS.FISHER.name:
            return self.character.lvl_fisher
        elif self.job == JOBS.MINER.name:
            return self.character.lvl_miner

        elif self.job == JOBS.WARRIOR.name:
            return self.character.lvl_marauder
        elif self.job == JOBS.PALADIN.name:
            return self.character.lvl_gladiator
        elif self.job == JOBS.MONK.name:
            return self.character.lvl_pugilist
        elif self.job == JOBS.DRAGOON.name:
            return self.character.lvl_lancer
        elif self.job == JOBS.BARD.name:
            return self.character.lvl_archer
        elif self.job == JOBS.WHITEMAGE.name:
            return self.character.lvl_conjurer
        elif self.job == JOBS.BLACKMAGE.name:
            return self.character.lvl_thaumaturge
        elif self.job == JOBS.SUMMONER.name:
            return self.character.lvl_arcanist
        elif self.job == JOBS.SCHOLAR.name:
            return self.character.lvl_arcanist
        elif self.job == JOBS.NINJA.name:
            return self.character.lvl_rogue

        elif self.job == JOBS.DARKNIGHT.name:
            return self.character.lvl_darknight
        elif self.job == JOBS.ASTROLOGIAN.name:
            return self.character.lvl_astrologian
        elif self.job == JOBS.MACHINIST.name:
            return self.character.lvl_machinist

        else:
            logging.error('Job instance is malformed: job = %s', self.job)
            return 0

    @property
    def as_dict(self):
        """


        :return: Dictionary of the the class' values for easier JSON serialization
        """
        items = list(map(lambda x: x.as_dict, list(self.items.all()))) if len(self.items.all()) > 0 else []

        return {
            'job': JOBS[self.job].value,
            'level': self.level,
            'items': items,
            'stats': {
                'hp': self.hp,
                'mp': self.mp,
                'tp': self.tp
            },
            'attributes': {
                'strength': self.strength,
                'dexterity': self.dexterity,
                'vitality': self.vitality,
                'intelligence': self.intelligence,
                'mind': self.mind,
                'piety': self.piety
            },
            'properties': {
                'offensive': {
                    'accuracy': self.accuracy,
                    'critical_hit_rate': self.crit_rate,
                    'determination': self.determination
                },
                'defensive': {
                    'defense': self.defense,
                    'parry': self.parry,
                    'magic_defense': self.magic_defense
                },
                'physical': {
                    'attack_power': self.attack_power,
                    'skill_speed': self.skill_speed
                },
                'mental': {
                    'attack_magic_potency': self.attack_magic_potency,
                    'healing_magic_potency': self.healing_magic_potency,
                    'spell_speed': self.spell_speed
                }
            },
            'resistances': {
                'elemental': {
                    'fire': self.fire,
                    'ice': self.ice,
                    'wind': self.wind,
                    'earth': self.earth,
                    'lightning': self.lightning,
                    'water': self.water
                },
                'status': {
                    'slow': self.slow_resist,
                    'silence': self.silence_resist,
                    'blind': self.blind_resist,
                    'poison': self.poison_resist,
                    'stun': self.stun_resist,
                    'sleep': self.sleep_resist,
                    'bind': self.bind_resist,
                    'heavy': self.heavy_resist
                },
                'physical': {
                    'slashing': self.slashing_resist,
                    'piercing': self.piercing_resist,
                    'blunt': self.blunt_resist
                }
            }
        }

    def __str__(self):
        return '{character} > {job}'.format(
            character=self.character.name,
            job=self.job
        )

    def __repr__(self):
        return '<Job char={character} job={} charid={}>'.format(
            character=self.character.name,
            job=self.job,
            charid=self.character.lodestone_id
        )


class FreeCompany(models.Model):
    """
    Free Company which contains at least one :class:`api.models.Character` and its associated stats

    Generated and added to DB by :func:`api.scrapers.free_company.scrape_free_company_by_id`.
    """

    name = models.CharField(max_length=100, default='')
    """
    :type: String
    """

    server = models.CharField(max_length=100, default='')
    """
    :type: String
    """

    members = models.ManyToManyField(Character)
    """
    Members of the free company

    :type: :class:`api.models.Character`
    """

    lodestone_id = models.CharField(max_length=200, unique=True)
    """
    Numeric ID unique for each free company

    Used to scrape the free company's info from Lodestone, see below.

    .. image:: ../../images/free_company_lodestone_id.PNG

    :type: String
    """

    tag = models.CharField(max_length=20)
    """
    :type: String
    """

    formed = models.DateField()
    """
    :type: DateTime
    """

    rank = models.IntegerField()
    """
    Reward rank (max 8). See `wiki <http://ffxiv.consolegameswiki.com/wiki/Free_Company#Free_Company_Entitlements>`_.

    :type: Int
    """

    weekly_rank = models.IntegerField()
    """
    World standings (previous week)

    :type: Int
    """

    monthly_rank = models.IntegerField()
    """
    World standings (previous month)

    :type: Int
    """

    slogan = models.CharField(max_length=200)
    """
    :type: String
    """

    @property
    def as_dict(self):
        """
        :return: Dictionary of the the class' values for easier JSON serialization
        """

        return {}
