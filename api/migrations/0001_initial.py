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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('lodestone_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('server', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=100)),
                ('city_state', models.CharField(max_length=100)),
                ('free_company', models.CharField(max_length=100)),
                ('grand_company', models.CharField(max_length=100, default='')),
            ],
        ),
    ]
