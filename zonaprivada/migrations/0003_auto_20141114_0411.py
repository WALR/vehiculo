# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zonaprivada', '0002_localidad_ruta_vehiculo'),
    ]

    operations = [
        migrations.CreateModel(
            name='incidencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=80)),
                ('observacion', models.CharField(max_length=150)),
                ('fecha', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='viaje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.CharField(max_length=30)),
                ('empleado', models.ForeignKey(to='zonaprivada.empleado')),
                ('ruta', models.ForeignKey(to='zonaprivada.ruta')),
                ('vehiculo', models.ForeignKey(to='zonaprivada.vehiculo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='incidencia',
            name='viaje',
            field=models.ForeignKey(to='zonaprivada.viaje'),
            preserve_default=True,
        ),
    ]
