# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150310_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('content', models.ImageField(upload_to='blog/image')),
                ('post', models.OneToOneField(to='blog.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContentText',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('content', models.TextField(default='')),
                ('post', models.OneToOneField(to='blog.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContentVoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('content', models.FileField(upload_to='blog/voice')),
                ('post', models.OneToOneField(to='blog.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='post',
            old_name='date',
            new_name='datetime',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
    ]
