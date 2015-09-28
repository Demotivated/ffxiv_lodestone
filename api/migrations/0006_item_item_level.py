# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20150927_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_level',
            field=models.IntegerField(default=0),
        ),
    ]
