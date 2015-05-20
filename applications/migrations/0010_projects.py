# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0011_auto_20150419_1006'),
        ('applications', '0009_service_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('status', models.BooleanField(verbose_name='Projecto activo', default=False)),
                ('order', models.PositiveIntegerField(verbose_name='Orden')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('description', cms.models.fields.PlaceholderField(related_name='project_description', slotname='description', to='cms.Placeholder', null=True, editable=False)),
                ('image', cms.models.fields.PlaceholderField(related_name='project_image', slotname='image', to='cms.Placeholder', null=True, editable=False)),
                ('name', cms.models.fields.PlaceholderField(related_name='project_name', slotname='name', to='cms.Placeholder', null=True, editable=False)),
            ],
            options={
                'verbose_name': 'Projecto',
                'verbose_name_plural': 'Projectos',
            },
            bases=(models.Model,),
        ),
    ]
