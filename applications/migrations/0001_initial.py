# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=False, verbose_name='Servicio activo')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('icon', cms.models.fields.PlaceholderField(to='cms.Placeholder', slotname='placeholder_icon', editable=False, null=True)),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
            },
            bases=(models.Model,),
        ),
    ]
