# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sangbok', '0009_auto_20150403_2246'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snapsvisa',
            options={'ordering': ['category', 'date_uploaded']},
        ),
    ]
