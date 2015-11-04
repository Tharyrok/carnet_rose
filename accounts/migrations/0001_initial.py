# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=500)),
                ('amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('kind', models.CharField(max_length=6, choices=[(b'credit', b'Cr\xc3\xa9dit'), (b'debit', b'D\xc3\xa9bit')])),
                ('comment', models.TextField(null=True, blank=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
