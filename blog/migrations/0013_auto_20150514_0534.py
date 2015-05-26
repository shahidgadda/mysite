# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20150513_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imag',
            field=models.ImageField(default=b'', upload_to=b'media/pics', blank=True),
        ),
    ]
