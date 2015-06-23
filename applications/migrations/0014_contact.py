# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0013_auto_20150521_2313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='Nombre', max_length=80)),
                ('email', models.EmailField(verbose_name='Email', max_length=300)),
                ('observations', models.TextField(verbose_name='Observaciones', max_length=2000)),
            ],
            options={
                'verbose_name_plural': 'Contactos',
                'verbose_name': 'Contacto',
            },
            bases=(models.Model,),
        ),
    ]
