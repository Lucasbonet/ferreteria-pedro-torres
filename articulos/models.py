# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Productos(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField (max_length=200)
    precio= models.CharField(max_length=200)
    detalles= models.TextField(blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.nombre