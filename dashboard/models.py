from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('nome', max_length=100, null=False)
    email = models.EmailField('e-mail')
