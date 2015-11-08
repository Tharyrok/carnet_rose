# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_movement_bank_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
            ],
        ),
    ]
