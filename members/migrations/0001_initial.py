# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255, verbose_name=b'Pr\xc3\xa9nom')),
                ('last_name', models.CharField(max_length=255, verbose_name=b'Nom')),
                ('last_paid_date', models.DateField(null=True, verbose_name=b'Derni\xc3\xa8re date de versement de la costisation', blank=True)),
                ('juridical_form', models.CharField(default=b'pp', help_text=b"99% du du temps ce sera 'personne physique' (un individu)", max_length=3, verbose_name=b'Forme juridique', choices=[(b'pp', b'Personne physique'), (b'pm', b'Personne morale')])),
                ('address', models.CharField(max_length=500, null=True, verbose_name=b"Lieu d'envoie du courrier", blank=True)),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
                ('member_since', models.DateField(default=datetime.datetime.today, verbose_name=b'Membre depuis le')),
                ('member_end', models.DateField(null=True, verbose_name=b"N'est plus membre depuis", blank=True)),
                ('why_member_end', models.TextField(null=True, verbose_name=b"Pourquoi il n'est plus membre", blank=True)),
                ('ca_member', models.BooleanField(default=False, verbose_name=b"Membre du conseil d'administration ?")),
                ('ca_function', models.CharField(max_length=255, null=True, verbose_name=b"R\xc3\xb4le dans le conseil d'administration", blank=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
            bases=(models.Model,),
        ),
    ]
