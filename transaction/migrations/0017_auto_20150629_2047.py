# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0016_auto_20150629_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 29, 20, 47, 55, 740633, tzinfo=utc)),
        ),
    ]
