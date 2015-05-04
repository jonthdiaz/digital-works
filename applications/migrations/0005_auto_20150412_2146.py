# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0004_auto_20150412_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='description',
            field=cms.models.fields.PlaceholderField(to='cms.Placeholder', slotname='description', null=True, editable=False, related_name='service_description'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=cms.models.fields.PlaceholderField(to='cms.Placeholder', slotname='icon', null=True, editable=False, related_name='service_icon'),
            preserve_default=True,
        ),
    ]
