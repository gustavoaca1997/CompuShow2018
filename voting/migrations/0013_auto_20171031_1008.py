# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-31 14:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0012_auto_20171031_0855'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='nominee',
            unique_together=set([]),
        ),
    ]
