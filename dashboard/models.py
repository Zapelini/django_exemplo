from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('nome', max_length=100, null=False)
    email = models.EmailField('e-mail')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __unicode__(self):
        return '%s - %s' % (self.name, self.email)


class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('nome', max_length=100, null=False)
    model = models.CharField('model', max_length=100, null=False)
    year = models.CharField('model', max_length=4)

    def __unicode__(self):
        return '%s - %s - %s' % (self.name, self.model, self.year)
