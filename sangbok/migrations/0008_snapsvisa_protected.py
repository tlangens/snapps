# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sangbok', '0007_auto_20150325_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='snapsvisa',
            name='protected',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
