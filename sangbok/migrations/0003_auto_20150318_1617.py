# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sangbok', '0002_auto_20150316_1939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snapsvisa',
            name='author',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.AddField(
            model_name='snapsvisa',
            name='other',
            field=models.CharField(max_length=256, null=True),
            preserve_default=True,
        ),
    ]
