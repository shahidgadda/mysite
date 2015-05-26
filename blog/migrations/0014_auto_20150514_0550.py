# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20150514_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imag',
            field=models.ImageField(default=b'', upload_to=b'pics', blank=True),
        ),
    ]
