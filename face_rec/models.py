# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):

    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    photo = models.TextField()

    def __str__(self):
        return self.firstName + " " + self.lastName

class Ident(models.Model):
    photo = models.TextField()