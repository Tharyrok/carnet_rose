# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_billing_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='cube',
            field=models.BooleanField(default=False, verbose_name=b'poss\xc3\xa8de une brique'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='vpn',
            field=models.BooleanField(default=False, verbose_name=b'a un abonnement vpn'),
            preserve_default=True,
        ),
    ]
