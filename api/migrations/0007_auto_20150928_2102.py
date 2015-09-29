# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_item_item_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='determination',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='mind',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='spell_speed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='vitality',
            field=models.IntegerField(default=0),
        ),
    ]
