# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='tag',
            field=models.ForeignKey(null=True, to='questionapp.Tag'),
        ),
    ]
