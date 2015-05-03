# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('applications', '0005_auto_20150412_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='name',
            field=cms.models.fields.PlaceholderField(null=True, to='cms.Placeholder', editable=False, related_name='service_name', slotname='name'),
            preserve_default=True,
        ),
    ]
