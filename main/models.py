# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class listedTransfers(models.Model):
    seller = models.CharField(max_length=200)
    buyer = models.CharField(max_length=200)
    domain =  models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    ts = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.domain 

class domainHistory(models.Model):
    domain = models.ForeignKey(listedTransfers)
    currentOwner = models.CharField(max_length=200)