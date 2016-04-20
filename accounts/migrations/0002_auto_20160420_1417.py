# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moocuser',
            name='email',
            field=models.EmailField(unique=True, max_length=254, verbose_name='Email address'),
        ),
    ]
