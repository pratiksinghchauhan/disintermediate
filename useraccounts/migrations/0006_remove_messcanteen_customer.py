# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-02-01 19:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0005_auto_20180201_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messcanteen',
            name='customer',
        ),
    ]
