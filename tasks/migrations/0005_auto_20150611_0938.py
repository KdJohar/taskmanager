# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20150611_0559'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-date_added']},
        ),
        migrations.AlterField(
            model_name='task',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
    ]
