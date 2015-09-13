# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
        migrations.RenameModel(
            old_name='Schedules',
            new_name='Schedule',
        ),
    ]
