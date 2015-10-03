# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140, db_index=True)),
                ('music', models.FileField(null=True, upload_to=b'board/tag_music')),
                ('background_color', models.CharField(default=b'101010', max_length=6)),
                ('text_color', models.CharField(default=b'FFFFFF', max_length=6)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=b'board/post_image'),
        ),
        migrations.AddField(
            model_name='tag',
            name='posts',
            field=models.ManyToManyField(related_name='tags', to='board.Post'),
        ),
    ]
