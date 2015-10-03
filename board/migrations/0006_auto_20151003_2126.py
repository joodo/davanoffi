# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_auto_20151003_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='parent',
            field=models.ForeignKey(related_name='comments', blank=True, to='board.Post', null=True),
        ),
    ]
