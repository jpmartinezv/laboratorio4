from django.db import models
from django.core.urlresolvers import reverse

class Cashier(models.Model):
    attendant = models.CharField(max_length=100, blank=True)
    store = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return self.store

    def get_absolute_url(self):
        return reverse('cashier:cashier_edit', kwargs={'pk': self.pk})
