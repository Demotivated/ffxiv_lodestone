# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150926_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='auto_attack',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='block_rate',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='block_strength',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='damage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='defense',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='delay',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='item_type',
            field=models.CharField(default='Body', max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='magic_defense',
            field=models.IntegerField(default=0),
        ),
    ]
