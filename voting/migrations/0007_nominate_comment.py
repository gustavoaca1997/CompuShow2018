# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-16 05:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0006_remove_category_inv'),
    ]

    operations = [
        migrations.AddField(
            model_name='nominate',
            name='comment',
            field=models.TextField(null=True),
        ),
    ]
