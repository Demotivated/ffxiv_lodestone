# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150914_0038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alchemist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('level', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Arcanist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('level', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Archer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('level', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Armorer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('level', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Astrologian',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('level', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Blacksmith',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('level', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Botanist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('level', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Carpenter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('level', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Conjurer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('level', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Culinarian',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('level', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DarkNight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('level', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Fisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('level', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Gladiator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('level', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Goldsmith',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('level', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Lancer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('level', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Leatherworker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('level', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Machinist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('level', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Marauder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('level', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Miner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('level', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pugilist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('level', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rogue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('level', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Thaumaturge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('level', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Weaver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('level', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='character',
            name='lvl_alchemist',
        ),
        migrations.RemoveField(
            model_name='character',
            name='lvl_arcanist',
        ),
        migrations.RemoveField(
            model_name='character',
            name='lvl_archer',
        ),
        migrations.RemoveField(
            model_name='character',
            name='lvl_armorer',
        ),
        migrations.RemoveField(
            model_name='character',
            name='lvl_astrologian',
        ),
        migrations.RemoveField(
            model_name='character',
            name='lvl_blacksmith',
        ),
        migrations.RemoveField(
            model_name='character',
            name='lvl_botanist',
        ),
        migrations.RemoveField(
            model_name='character',
            name='lvl_carpenter',
        ),
        migrations.RemoveField(
            model_name='character',
            name='lvl_conjurer',
        ),
        migrations.RemoveField(
            model_name='character',
            name='lvl_culinarian',
        ),
        migrations.RemoveField(
            model_name='character',
            name='lvl_dark_night',
        ),
        migrations.RemoveField(
            model_name='character',
            name='lvl_fisher',
        ),
        migrations.RemoveField(
            model_name='character',
            name='lvl_gladiator',
        ),
        migrations.RemoveField(
            model_name='character',
            name='lvl_goldsmith',
        ),
        migrations.RemoveField(
            model_name='character',
            name='lvl_lancer',
        ),
        migrations.RemoveField(
            model_name='character',
            name='lvl_leatherworker',
        ),
        migrations.RemoveField(
            model_name='character',
            name='lvl_machinist',
        ),
        migrations.RemoveField(
            model_name='character',
            name='lvl_marauder',
        ),
        migrations.RemoveField(
            model_name='character',
            name='lvl_miner',
        ),
        migrations.RemoveField(
            model_name='character',
            name='lvl_pugilist',
        ),
        migrations.RemoveField(
            model_name='character',
            name='lvl_rogue',
        ),
        migrations.RemoveField(
            model_name='character',
            name='lvl_thaumaturge',
        ),
        migrations.RemoveField(
            model_name='character',
            name='lvl_weaver',
        ),
        migrations.AlterField(
            model_name='character',
            name='city_state',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='character',
            name='free_company',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='character',
            name='lodestone_id',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='character',
            name='server',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='character',
            name='species',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AddField(
            model_name='weaver',
            name='character',
            field=models.OneToOneField(to='api.Character'),
        ),
        migrations.AddField(
            model_name='thaumaturge',
            name='character',
            field=models.OneToOneField(to='api.Character'),
        ),
        migrations.AddField(
            model_name='rogue',
            name='character',
            field=models.OneToOneField(to='api.Character'),
        ),
        migrations.AddField(
            model_name='pugilist',
            name='character',
            field=models.OneToOneField(to='api.Character'),
        ),
        migrations.AddField(
            model_name='miner',
            name='character',
            field=models.OneToOneField(to='api.Character'),
        ),
        migrations.AddField(
            model_name='marauder',
            name='character',
            field=models.OneToOneField(to='api.Character'),
        ),
        migrations.AddField(
            model_name='machinist',
            name='character',
            field=models.OneToOneField(to='api.Character'),
        ),
        migrations.AddField(
            model_name='leatherworker',
            name='character',
            field=models.OneToOneField(to='api.Character'),
        ),
        migrations.AddField(
            model_name='lancer',
            name='character',
            field=models.OneToOneField(to='api.Character'),
        ),
        migrations.AddField(
            model_name='goldsmith',
            name='character',
            field=models.OneToOneField(to='api.Character'),
        ),
        migrations.AddField(
            model_name='gladiator',
            name='character',
            field=models.OneToOneField(to='api.Character'),
        ),
        migrations.AddField(
            model_name='fisher',
            name='character',
            field=models.OneToOneField(to='api.Character'),
        ),
        migrations.AddField(
            model_name='darknight',
            name='character',
            field=models.OneToOneField(to='api.Character'),
        ),
        migrations.AddField(
            model_name='culinarian',
            name='character',
            field=models.OneToOneField(to='api.Character'),
        ),
        migrations.AddField(
            model_name='conjurer',
            name='character',
            field=models.OneToOneField(to='api.Character'),
        ),
        migrations.AddField(
            model_name='carpenter',
            name='character',
            field=models.OneToOneField(to='api.Character'),
        ),
        migrations.AddField(
            model_name='botanist',
            name='character',
            field=models.OneToOneField(to='api.Character'),
        ),
        migrations.AddField(
            model_name='blacksmith',
            name='character',
            field=models.OneToOneField(to='api.Character'),
        ),
        migrations.AddField(
            model_name='astrologian',
            name='character',
            field=models.OneToOneField(to='api.Character'),
        ),
        migrations.AddField(
            model_name='armorer',
            name='character',
            field=models.OneToOneField(to='api.Character'),
        ),
        migrations.AddField(
            model_name='archer',
            name='character',
            field=models.OneToOneField(to='api.Character'),
        ),
        migrations.AddField(
            model_name='arcanist',
            name='character',
            field=models.OneToOneField(to='api.Character'),
        ),
        migrations.AddField(
            model_name='alchemist',
            name='character',
            field=models.OneToOneField(to='api.Character'),
        ),
    ]
