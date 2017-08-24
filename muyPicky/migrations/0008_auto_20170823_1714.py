# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 00:14
from __future__ import unicode_literals

from django.db import migrations, models
import muyPicky.validators


class Migration(migrations.Migration):

    dependencies = [
        ('muyPicky', '0007_restaurantlocation_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantlocation',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[muyPicky.validators.validate_category]),
        ),
    ]
