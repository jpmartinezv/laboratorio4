# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0004_auto_20150629_1640'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='idaccount',
            new_name='account',
        ),
    ]
