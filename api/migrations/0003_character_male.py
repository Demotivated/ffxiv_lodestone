# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_character_grand_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='male',
            field=models.BooleanField(default=True),
        ),
    ]
