from django.db import models
from django.core.urlresolvers import reverse
from client.models import Client
from cashier.models import Cashier

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client)
    cashier = models.ForeignKey(Cashier, null=True)
    status = models.BooleanField(default=True)
    amount = models.FloatField(default=0.0)

    def __unicode__(self):
        return self.client.firstName + ' ' + self.client.lastName + ' ' +str(self.id)

    def get_absolute_url(self):
        return reverse('client:client_edit', kwargs={'pk': self.pk})
