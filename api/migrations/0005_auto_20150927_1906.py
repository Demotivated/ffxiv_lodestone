# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20150927_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job',
            field=models.CharField(choices=[('MARAUDER', 'Marauder'), ('GLADIATOR', 'Gladiator'), ('PUGILIST', 'Pugilist'), ('LANCER', 'Lancer'), ('ARCHER', 'Archer'), ('ROGUE', 'Rogue'), ('CONJURER', 'Conjurer'), ('THAUMATURGE', 'Thaumaturge'), ('ARCANIST', 'Arcanist'), ('CARPENTER', 'Carpenter'), ('BLACKSMITH', 'Blacksmith'), ('ARMORER', 'Armorer'), ('GOLDSMITH', 'Goldsmith'), ('LEATHERWORKER', 'Leatherworker'), ('WEAVER', 'Weaver'), ('ALCHEMIST', 'Alchemist'), ('CULINARIAN', 'Culinarian'), ('BOTANIST', 'Botanist'), ('FISHER', 'Fisher'), ('MINER', ' Miner'), ('WARRIOR', 'Warrior'), ('PALADIN', 'Paladin'), ('MONK', 'Monk'), ('DRAGOON', 'Dragoon'), ('BARD', 'Bard'), ('NINJA', 'Ninja'), ('WHITEMAGE', 'White Mage'), ('BLACKMAGE', 'Black Mage'), ('SUMMONER', 'Summoner'), ('SCHOLAR', 'Scholar'), ('DARKNIGHT', 'Dark Knight'), ('ASTROLOGIAN', 'Astrologian'), ('MACHINIST', 'Machinist')], max_length=25),
        ),
    ]
