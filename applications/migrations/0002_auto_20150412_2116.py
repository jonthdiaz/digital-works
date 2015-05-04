# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=cms.models.fields.PlaceholderField(to='cms.Placeholder', slotname='icon', null=True, editable=False),
            preserve_default=True,
        ),
    ]
