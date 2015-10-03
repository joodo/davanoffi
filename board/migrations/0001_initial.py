# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=140, null=True)),
                ('content', models.TextField(null=True)),
                ('image', models.ImageField(null=True, upload_to=b'board/image')),
                ('parent', models.ForeignKey(related_name='comments', to='board.Post', null=True)),
            ],
        ),
    ]
