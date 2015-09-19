# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150917_2307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('lodestone_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='alchemist',
            name='items',
            field=models.ManyToManyField(to='api.Item'),
        ),
        migrations.AddField(
            model_name='arcanist',
            name='items',
            field=models.ManyToManyField(to='api.Item'),
        ),
        migrations.AddField(
            model_name='archer',
            name='items',
            field=models.ManyToManyField(to='api.Item'),
        ),
        migrations.AddField(
            model_name='armorer',
            name='items',
            field=models.ManyToManyField(to='api.Item'),
        ),
        migrations.AddField(
            model_name='astrologian',
            name='items',
            field=models.ManyToManyField(to='api.Item'),
        ),
        migrations.AddField(
            model_name='blacksmith',
            name='items',
            field=models.ManyToManyField(to='api.Item'),
        ),
        migrations.AddField(
            model_name='botanist',
            name='items',
            field=models.ManyToManyField(to='api.Item'),
        ),
        migrations.AddField(
            model_name='carpenter',
            name='items',
            field=models.ManyToManyField(to='api.Item'),
        ),
        migrations.AddField(
            model_name='conjurer',
            name='items',
            field=models.ManyToManyField(to='api.Item'),
        ),
        migrations.AddField(
            model_name='culinarian',
            name='items',
            field=models.ManyToManyField(to='api.Item'),
        ),
        migrations.AddField(
            model_name='darknight',
            name='items',
            field=models.ManyToManyField(to='api.Item'),
        ),
        migrations.AddField(
            model_name='fisher',
            name='items',
            field=models.ManyToManyField(to='api.Item'),
        ),
        migrations.AddField(
            model_name='gladiator',
            name='items',
            field=models.ManyToManyField(to='api.Item'),
        ),
        migrations.AddField(
            model_name='goldsmith',
            name='items',
            field=models.ManyToManyField(to='api.Item'),
        ),
        migrations.AddField(
            model_name='lancer',
            name='items',
            field=models.ManyToManyField(to='api.Item'),
        ),
        migrations.AddField(
            model_name='leatherworker',
            name='items',
            field=models.ManyToManyField(to='api.Item'),
        ),
        migrations.AddField(
            model_name='machinist',
            name='items',
            field=models.ManyToManyField(to='api.Item'),
        ),
        migrations.AddField(
            model_name='marauder',
            name='items',
            field=models.ManyToManyField(to='api.Item'),
        ),
        migrations.AddField(
            model_name='miner',
            name='items',
            field=models.ManyToManyField(to='api.Item'),
        ),
        migrations.AddField(
            model_name='pugilist',
            name='items',
            field=models.ManyToManyField(to='api.Item'),
        ),
        migrations.AddField(
            model_name='rogue',
            name='items',
            field=models.ManyToManyField(to='api.Item'),
        ),
        migrations.AddField(
            model_name='thaumaturge',
            name='items',
            field=models.ManyToManyField(to='api.Item'),
        ),
        migrations.AddField(
            model_name='weaver',
            name='items',
            field=models.ManyToManyField(to='api.Item'),
        ),
    ]
