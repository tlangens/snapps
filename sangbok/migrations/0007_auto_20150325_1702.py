# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sangbok', '0006_auto_20150322_0855'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snapsvisa',
            old_name='other',
            new_name='post',
        ),
        migrations.AddField(
            model_name='snapsvisa',
            name='pre',
            field=models.CharField(max_length=256, default='', blank=True),
            preserve_default=False,
        ),
    ]
