# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sangbok', '0004_auto_20150318_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snapsvisa',
            name='other',
            field=models.CharField(max_length=256, blank=True, default=''),
            preserve_default=True,
        ),
    ]
