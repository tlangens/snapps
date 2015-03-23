# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sangbok', '0005_auto_20150319_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snapsvisa',
            name='category',
            field=models.ForeignKey(to='sangbok.Category', default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='snapsvisa',
            name='other',
            field=models.CharField(max_length=256, blank=True),
            preserve_default=True,
        ),
    ]
