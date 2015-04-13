# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0002_auto_20150412_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=cms.models.fields.PlaceholderField(null=True, slotname='placeholder_icon', to='cms.Placeholder', editable=False),
            preserve_default=True,
        ),
    ]
