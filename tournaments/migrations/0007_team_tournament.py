# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0006_tournament'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='tournament',
            field=models.ForeignKey(to='tournaments.Tournament', default=None),
            preserve_default=True,
        ),
    ]
