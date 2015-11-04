# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20150517_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='comments',
            field=models.TextField(help_text=b"Random comments regarding the current situation of this member like 'paying vpn by cash' or sometehing like that.", null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='is_not_a_member_yet',
            field=models.BooleanField(default=False, help_text=b"Cette personne a command\xc3\xa9 une brique avec un access VPN mais n'a pas envoy\xc3\xa9 commenc\xc3\xa9 \xc3\xa0 payer son abonnement VPN mais doit le faire. Elle sera consid\xc3\xa9r\xc3\xa9 comme membre quand \xc3\xa7a sera fait."),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='member_since',
            field=models.DateField(default=datetime.datetime.today, null=True, verbose_name=b'Membre depuis le', blank=True),
            preserve_default=True,
        ),
    ]
