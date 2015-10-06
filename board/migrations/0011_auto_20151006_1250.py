# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0010_auto_20151004_1041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='music',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='text_color',
        ),
        migrations.AddField(
            model_name='post',
            name='music',
            field=models.FileField(upload_to=b'board/post_music', blank=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='content_text_color',
            field=models.CharField(default=b'#FFFFFF', max_length=6),
        ),
        migrations.AddField(
            model_name='tag',
            name='title_text_color',
            field=models.CharField(default=b'cray', max_length=6),
        ),
        migrations.AlterField(
            model_name='tag',
            name='background_color',
            field=models.CharField(default=b'#101010', max_length=6),
        ),
    ]
