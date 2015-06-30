from django.db import models
from django.core.urlresolvers import reverse

class Client(models.Model):
    firstName = models.CharField(max_length=100, blank=True)
    lastName = models.CharField(max_length=100, blank=True)
    dni = models.CharField(max_length=9, blank=True)
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    email = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        return self.firstName + " " + self.lastName

    def get_absolute_url(self):
        return reverse('client:client_edit', kwargs={'pk': self.pk})
