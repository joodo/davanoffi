# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150311_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentimage',
            name='title',
        ),
        migrations.RemoveField(
            model_name='contenttext',
            name='title',
        ),
        migrations.RemoveField(
            model_name='contentvoice',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=140, default=''),
            preserve_default=True,
        ),
    ]
