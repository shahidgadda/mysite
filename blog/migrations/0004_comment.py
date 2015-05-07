# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150504_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(serialize=False, primary_key=True)),
                ('author', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=75)),
                ('title', models.ForeignKey(to='blog.Post')),
            ],
            options={
                'db_table': 'comment',
            },
            bases=(models.Model,),
        ),
    ]
