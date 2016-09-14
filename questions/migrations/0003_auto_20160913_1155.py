# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-13 11:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20160913_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='categorie',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='questions.Categorie'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='meta_description',
            field=models.TextField(blank=True, max_length=155, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='reponse',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]