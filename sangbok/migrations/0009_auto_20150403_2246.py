# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sangbok', '0008_snapsvisa_protected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snapsvisa',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='snapsvisa',
            name='date_uploaded',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
