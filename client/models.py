from django.db import models
from django.core.urlresolvers import reverse

class Client(models.Model):
    firstName = models.CharField(max_length = 100)
    lastName = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.firstName

    def get_absolute_url(self):
        return reverse('client:client_edit', kwargs={'pk': self.pk})