# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='account',
            name='test',
        ),
        migrations.AddField(
            model_name='account',
            name='status',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
