# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-03-30 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0175_auto_20191230_2354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finalapplication',
            name='time_commitment_updates',
        ),
        migrations.RemoveField(
            model_name='finalapplication',
            name='time_commitments_correct',
        ),
        migrations.AddField(
            model_name='finalapplication',
            name='time_correct',
            field=models.BooleanField(default=False, help_text='If any time commitments (like a job or school) are missing, say no. If any start or end dates are incorrect, say no.', verbose_name='Are the time commitments listed above correct?'),
        ),
        migrations.AddField(
            model_name='finalapplication',
            name='time_updates',
            field=models.TextField(blank=True, help_text='Make sure your time commitments lists any current or future jobs you have, even if you are taking a leave of absence.', max_length=8000, verbose_name='(Optional) If your time commitments are incorrect or have changed, please provide your updated time commitments. **Please leave this blank if your time commitments are correct.**'),
        ),
    ]
