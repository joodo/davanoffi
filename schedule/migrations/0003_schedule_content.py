# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_auto_20150309_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='content',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
    ]
