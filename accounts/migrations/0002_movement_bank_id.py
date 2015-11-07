# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movement',
            name='bank_id',
            field=models.CharField(max_length=255, unique=True, null=True, editable=False, blank=True),
        ),
    ]
