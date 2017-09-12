# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_electricityusage_waterusage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='electricityusage',
            old_name='occurences_per_week',
            new_name='occurrences_per_week',
        ),
    ]
