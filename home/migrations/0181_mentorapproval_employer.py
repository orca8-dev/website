# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-02 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0180_auto_20200731_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentorapproval',
            name='employer',
            field=models.CharField(default='Prefer not to say', max_length=100, verbose_name='Employer'),
            preserve_default=False,
        ),
    ]