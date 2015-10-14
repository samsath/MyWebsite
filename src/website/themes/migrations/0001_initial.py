# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Themes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'Title')),
                ('sort_value', models.IntegerField(null=True, blank=True)),
                ('is_public', models.BooleanField(default=False)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('slug', django_extensions.db.fields.AutoSlugField(editable=False, populate_from=(b'title',), blank=True, unique=True)),
            ],
            options={
                'ordering': ['sort_value'],
                'verbose_name': 'Themes',
                'verbose_name_plural': 'Themes',
            },
            bases=(models.Model,),
        ),
    ]
