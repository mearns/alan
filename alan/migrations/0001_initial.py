# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import alan.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'A name used to identify this task. Should provide a terse summary of the task.', max_length=255)),
                ('description', alan.models.MarkupTextField(help_text=b'Describe the work to be done in sufficient detail that it can be completed.', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
