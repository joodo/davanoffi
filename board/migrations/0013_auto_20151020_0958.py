# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0012_auto_20151013_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='anchor_text_color',
            field=models.CharField(default=b'#5F9EA0', max_length=30),
        ),
        migrations.AlterField(
            model_name='tag',
            name='background_color',
            field=models.CharField(default=b'#101010', max_length=30),
        ),
        migrations.AlterField(
            model_name='tag',
            name='content_text_color',
            field=models.CharField(default=b'#FFFFFF', max_length=30),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title_text_color',
            field=models.CharField(default=b'#808080', max_length=30),
        ),
    ]
