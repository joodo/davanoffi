# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_post_total_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default='', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default=None, upload_to=b'board/post_image', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='parent',
            field=models.ForeignKey(related_name='comments', default=None, blank=True, to='board.Post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default=None, max_length=140, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='total_length',
            field=models.IntegerField(blank=True),
        ),
    ]
