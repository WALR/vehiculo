# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zonapublica', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rutainteres',
            name='estado',
        ),
        migrations.AddField(
            model_name='rutainteres',
            name='leido_estado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rutainteres',
            name='nombre',
            field=models.CharField(default=b'Nombre Ruta', max_length=150),
            preserve_default=True,
        ),
    ]
