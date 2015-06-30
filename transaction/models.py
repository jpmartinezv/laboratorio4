from django.db import models
from django.core.urlresolvers import reverse
from account.models import Account
from datetime import date

class Transaction(models.Model):
    account = models.ForeignKey(Account)
    date = models.DateField(default=date.today())
    TYPE_TRANSACTION = (
        ('AP', 'Apertura'),
        ('DE', 'Deposito'),
        ('RE', 'Retiro'),
        ('PL', 'Pago de luz'),
        ('PA', 'Pago de agua'),
        ('TS', 'Transferencia como salida'),
        ('TI', 'Transferencia como ingreso'),
    )
    type = models.CharField(max_length=2, choices=TYPE_TRANSACTION, default='AP')
    amount = models.FloatField()
    destination = models.CharField(max_length=50)

    def __unicode__(self):
        return str(self.id) + ' ' + self.type

    def get_absolute_url(self):
        return reverse('transaction:transaction_edit', kwargs={'pk': self.pk})
