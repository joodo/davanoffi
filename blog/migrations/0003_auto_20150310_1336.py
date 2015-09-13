# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150310_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(choices=[('XU', 'just'), ('JO', 'friend')], max_length=2, default='XU'),
            preserve_default=True,
        ),
    ]
