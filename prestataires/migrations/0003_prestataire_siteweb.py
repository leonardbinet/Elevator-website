# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-19 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestataires', '0002_auto_20160919_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestataire',
            name='siteweb',
            field=models.URLField(blank=True, default=''),
        ),
    ]
