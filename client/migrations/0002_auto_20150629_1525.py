# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='address',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='client',
            name='dni',
            field=models.CharField(max_length=9, blank=True),
        ),
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='firstName',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='lastName',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
