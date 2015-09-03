# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lodestone_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('server', models.CharField(max_length=20)),
                ('species', models.CharField(max_length=20)),
                ('city_state', models.CharField(max_length=20)),
                ('free_company', models.CharField(max_length=100)),
            ],
        ),
    ]
