# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pessoa',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('pessoa_nome', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ramal',
            fields=[
                ('Ramal_id', models.AutoField(serialize=False, primary_key=True)),
                ('Ramal_Number', models.CharField(max_length=5)),
            ],
        ),
    ]
