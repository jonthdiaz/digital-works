# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0007_auto_20150412_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='name',
            field=cms.models.fields.PlaceholderField(to='cms.Placeholder', editable=False, related_name='service_name', slotname='name', null=True),
            preserve_default=True,
        ),
    ]
