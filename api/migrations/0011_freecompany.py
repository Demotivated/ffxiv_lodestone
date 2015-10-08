# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20150929_0049'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreeCompany',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(default='', max_length=100)),
                ('server', models.CharField(default='', max_length=100)),
                ('lodestone_id', models.CharField(unique=True, max_length=200)),
                ('tag', models.CharField(max_length=20)),
                ('formed', models.DateField()),
                ('rank', models.IntegerField()),
                ('weekly_rank', models.IntegerField()),
                ('monthly_rank', models.IntegerField()),
                ('slogan', models.CharField(max_length=200)),
                ('members', models.ManyToManyField(to='api.Character')),
            ],
        ),
    ]
