# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='textcontent',
            name='post',
        ),
        migrations.DeleteModel(
            name='TextContent',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_date',
            new_name='date',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=2, default='XU', choices=[('TXT', 'Text'), ('IMG', 'Image'), ('VOI', 'Voice')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(max_length=3, default='TXT', choices=[('TXT', 'Text'), ('IMG', 'Image'), ('VOI', 'Voice')]),
            preserve_default=True,
        ),
    ]
