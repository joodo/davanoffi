# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20151002_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='total_length',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
