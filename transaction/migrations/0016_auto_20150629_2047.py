# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0015_auto_20150629_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.CharField(default=b'AP', max_length=2, choices=[(b'AP', b'Apertura'), (b'DE', b'Deposito'), (b'RE', b'Retiro'), (b'PL', b'Pago de luz'), (b'PA', b'Pago de agua'), (b'TS', b'Transferencia como salida'), (b'TI', b'Transferencia como ingreso')]),
        ),
    ]
