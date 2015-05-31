# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150531_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='creator',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, related_name='creators'),
        ),
    ]
