# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('applications', '0003_auto_20150412_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='description',
            field=cms.models.fields.PlaceholderField(null=True, slotname='description', related_name='description', editable=False, to='cms.Placeholder'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=cms.models.fields.PlaceholderField(null=True, slotname='icon', related_name='icon', editable=False, to='cms.Placeholder'),
            preserve_default=True,
        ),
    ]
