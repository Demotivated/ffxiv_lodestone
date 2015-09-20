# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20150918_1658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='grand_company',
            new_name='grand_company_name',
        ),
        migrations.AddField(
            model_name='character',
            name='grand_company_rank',
            field=models.CharField(max_length=100, default=''),
        ),
    ]
