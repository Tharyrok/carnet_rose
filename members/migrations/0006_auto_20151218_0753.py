# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20151104_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='added_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 18, 7, 53, 49, 771294), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 18, 7, 53, 54, 913906), auto_now=True),
            preserve_default=False,
        ),
    ]
