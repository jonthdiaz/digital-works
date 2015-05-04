# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0006_service_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='name',
            field=cms.models.fields.PlaceholderField(editable=False, slotname='icon', related_name='service_name', null=True, to='cms.Placeholder'),
            preserve_default=True,
        ),
    ]
