# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_auto_20150629_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='destination',
            field=models.CharField(max_length=50),
        ),
    ]
