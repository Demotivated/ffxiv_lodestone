# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20150928_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='accuracy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='critical_hit_rate',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='piety',
            field=models.IntegerField(default=0),
        ),
    ]
