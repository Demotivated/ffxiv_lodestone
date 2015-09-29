# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_character_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='free_company',
            new_name='free_company_name',
        ),
        migrations.AddField(
            model_name='character',
            name='free_company_id',
            field=models.CharField(default='', max_length=100),
        ),
    ]
