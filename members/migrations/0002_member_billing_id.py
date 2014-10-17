# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='billing_id',
            field=models.CharField(help_text=b"Identifiant donn\xc3\xa9 \xc3\xa0 l'usag\xc3\xa9 qu'il doit mettre sur ses virements (pour le VPN pour l'instant)", max_length=255, null=True, verbose_name=b'Identifiant de domiciliation', blank=True),
            preserve_default=True,
        ),
    ]
