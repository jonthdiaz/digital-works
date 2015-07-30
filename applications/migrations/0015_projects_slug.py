# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0014_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='slug',
            field=models.SlugField(max_length=300, blank=True, null=True),
            preserve_default=True,
        ),
    ]
