# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0011_auto_20151006_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='background_color',
            field=models.CharField(default=b'#101010', max_length=7),
        ),
        migrations.AlterField(
            model_name='tag',
            name='content_text_color',
            field=models.CharField(default=b'#FFFFFF', max_length=7),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=140, editable=False, db_index=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title_text_color',
            field=models.CharField(default=b'#808080', max_length=7),
        ),
    ]
