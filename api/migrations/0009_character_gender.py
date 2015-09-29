# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20150928_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='gender',
            field=models.CharField(max_length=20, default=''),
        ),
    ]
