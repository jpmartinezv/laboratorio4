# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashier', '0001_initial'),
        ('account', '0002_auto_20150624_0214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='idClient',
            new_name='client',
        ),
        migrations.AddField(
            model_name='account',
            name='amount',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='account',
            name='cashier',
            field=models.ForeignKey(to='cashier.Cashier', null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
