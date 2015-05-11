# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0008_auto_20150412_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='order',
            field=models.PositiveIntegerField(verbose_name='Orden', default=1),
            preserve_default=False,
        ),
    ]
