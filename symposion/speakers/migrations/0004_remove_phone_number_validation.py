# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-26 23:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_speakers', '0003_speaker_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='phone_number',
            field=models.CharField(max_length=40, verbose_name='Phone number'),
        ),
    ]