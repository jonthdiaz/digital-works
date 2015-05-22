# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0011_auto_20150419_1006'),
        ('applications', '0011_auto_20150518_2118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='Nombre cliente', max_length=300)),
                ('image', models.ImageField(verbose_name='image', upload_to='clients_images', blank=True, null=True)),
                ('phone', models.CharField(verbose_name='Teléfono cliente', max_length=30, blank=True, null=True)),
                ('address', models.CharField(verbose_name='Dirección', max_length=100, blank=True, null=True)),
                ('email', models.EmailField(verbose_name='Email', max_length=100, blank=True, null=True)),
                ('status', models.BooleanField(verbose_name='Cliente activo', default=True)),
                ('order', models.PositiveIntegerField(verbose_name='Orden')),
                ('date_added', models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)),
                ('description', cms.models.fields.PlaceholderField(to='cms.Placeholder', slotname='description', editable=False, null=True, related_name='client_description')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
            bases=(models.Model,),
        ),
    ]
