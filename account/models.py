from django.db import models
from django.core.urlresolvers import reverse
from client.models import Client

class Account(models.Model):
    idClient = models.ForeignKey(Client)
    status = models.BooleanField()

    def __unicode__(self):
        return self.idClient

    def get_absolute_url(self):
        return reverse('client:client_edit', kwargs={'pk': self.pk})