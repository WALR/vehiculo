# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zonaprivada', '0003_auto_20141114_0411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viaje',
            name='estado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
