# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0003_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='name',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
    ]
