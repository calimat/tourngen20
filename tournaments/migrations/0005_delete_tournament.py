# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0004_team_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tournament',
        ),
    ]
