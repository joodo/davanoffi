# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150311_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentimage',
            name='title',
            field=models.CharField(default='', max_length=140),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contenttext',
            name='title',
            field=models.CharField(default='', max_length=140),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contentvoice',
            name='title',
            field=models.CharField(default='', max_length=140),
            preserve_default=True,
        ),
    ]
