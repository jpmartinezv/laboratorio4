# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_auto_20150629_1632'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='account',
            new_name='idaccount',
        ),
    ]
