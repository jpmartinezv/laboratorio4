# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cashier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attendant', models.CharField(max_length=100, blank=True)),
                ('store', models.CharField(max_length=100, blank=True)),
                ('address', models.CharField(max_length=100, blank=True)),
            ],
        ),
    ]
