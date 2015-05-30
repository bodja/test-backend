# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
from django.conf import settings
import localflavor.generic.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, serialize=False, to=settings.AUTH_USER_MODEL, primary_key=True, parent_link=True)),
                ('iban', localflavor.generic.models.IBANField(max_length=34)),
                ('photo', models.ImageField(upload_to='media/accounts/picture/%Y/%m/%d', null=True)),
                ('creator', models.ForeignKey(to='accounts.Customer', null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
