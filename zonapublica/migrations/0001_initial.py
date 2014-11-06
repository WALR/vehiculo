# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rutaInteres',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField(max_length=200)),
                ('direccion', models.CharField(max_length=60, blank=True)),
                ('telefono', models.IntegerField(max_length=50, blank=True)),
                ('email', models.EmailField(max_length=50, blank=True)),
                ('fecha', models.DateField(max_length=50)),
                ('estado', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
