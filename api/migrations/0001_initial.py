# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('lodestone_id', models.CharField(default='', max_length=100)),
                ('server', models.CharField(default='', max_length=100)),
                ('species', models.CharField(default='', max_length=100)),
                ('city_state', models.CharField(default='', max_length=100)),
                ('free_company', models.CharField(default='', max_length=100)),
                ('grand_company_name', models.CharField(default='', max_length=100)),
                ('grand_company_rank', models.CharField(default='', max_length=100)),
                ('lvl_archer', models.IntegerField(default=0)),
                ('lvl_lancer', models.IntegerField(default=0)),
                ('lvl_marauder', models.IntegerField(default=0)),
                ('lvl_pugilist', models.IntegerField(default=0)),
                ('lvl_rogue', models.IntegerField(default=0)),
                ('lvl_arcanist', models.IntegerField(default=0)),
                ('lvl_conjurer', models.IntegerField(default=0)),
                ('lvl_thaumaturge', models.IntegerField(default=0)),
                ('lvl_astrologian', models.IntegerField(default=0)),
                ('lvl_darknight', models.IntegerField(default=0)),
                ('lvl_machinist', models.IntegerField(default=0)),
                ('lvl_alchemist', models.IntegerField(default=0)),
                ('lvl_armorer', models.IntegerField(default=0)),
                ('lvl_blacksmith', models.IntegerField(default=0)),
                ('lvl_carpenter', models.IntegerField(default=0)),
                ('lvl_culinarian', models.IntegerField(default=0)),
                ('lvl_gladiator', models.IntegerField(default=0)),
                ('lvl_goldsmith', models.IntegerField(default=0)),
                ('lvl_leatherworker', models.IntegerField(default=0)),
                ('lvl_weaver', models.IntegerField(default=0)),
                ('lvl_botanist', models.IntegerField(default=0)),
                ('lvl_fisher', models.IntegerField(default=0)),
                ('lvl_miner', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('lodestone_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('job', models.CharField(max_length=25)),
                ('character', models.ForeignKey(to='api.Character')),
                ('items', models.ManyToManyField(to='api.Item')),
            ],
        ),
    ]
