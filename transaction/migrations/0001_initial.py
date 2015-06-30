# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20150624_0214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('type', models.CharField(default=b'AP', max_length=2, choices=[(b'AP', b'Apertura'), (b'DE', b'Deposito'), (b'RE', b'Retiro')])),
                ('amount', models.FloatField()),
                ('destinatoin', models.CharField(max_length=100)),
                ('account', models.ForeignKey(to='account.Account')),
            ],
        ),
    ]
