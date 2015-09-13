# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150310_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(default='XU', choices=[('XU', 'friend'), ('JO', 'just')], max_length=2),
            preserve_default=True,
        ),
    ]
