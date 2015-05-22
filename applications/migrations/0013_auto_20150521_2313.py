# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0011_auto_20150419_1006'),
        ('applications', '0012_clients'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=300, verbose_name='Nombre cliente')),
                ('image', models.ImageField(upload_to='clients_images', null=True, verbose_name='image', blank=True)),
                ('phone', models.CharField(max_length=30, null=True, verbose_name='Teléfono cliente', blank=True)),
                ('address', models.CharField(max_length=100, null=True, verbose_name='Dirección', blank=True)),
                ('email', models.EmailField(max_length=100, null=True, verbose_name='Email', blank=True)),
                ('status', models.BooleanField(default=True, verbose_name='Cliente activo')),
                ('order', models.PositiveIntegerField(verbose_name='Orden')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('description', cms.models.fields.PlaceholderField(null=True, related_name='client_description', slotname='description', editable=False, to='cms.Placeholder')),
            ],
            options={
                'verbose_name_plural': 'Clientes',
                'verbose_name': 'Cliente',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='clients',
            name='description',
        ),
        migrations.DeleteModel(
            name='Clients',
        ),
    ]
