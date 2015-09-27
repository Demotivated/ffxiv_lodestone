# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150927_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='lodestone_id',
            field=models.CharField(max_length=100, default='', unique=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='lodestone_id',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
