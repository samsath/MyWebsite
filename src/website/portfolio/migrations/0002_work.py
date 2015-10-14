# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_auto_20151014_0030'),
        ('themes', '0001_initial'),
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'Title')),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('slug', django_extensions.db.fields.AutoSlugField(editable=False, populate_from=(b'title',), blank=True, unique=True)),
                ('headline', models.TextField(null=True, verbose_name='Headline', blank=True)),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('date', models.DateField(null=True, verbose_name='Date', blank=True)),
                ('is_public', models.BooleanField(default=False)),
                ('content', models.ManyToManyField(related_name='work_content', null=True, verbose_name=b'Content', to='file.File', blank=True)),
                ('cover', models.ForeignKey(related_name='cover_image', verbose_name=b'Cover', blank=True, to='file.File', null=True)),
                ('links', models.ManyToManyField(to='portfolio.Links', null=True, verbose_name=b'Links', blank=True)),
                ('related', models.ManyToManyField(related_name='related_rel_+', null=True, verbose_name=b'Related Work', to='portfolio.Work', blank=True)),
                ('themes', models.ManyToManyField(to='themes.Themes', null=True, verbose_name=b'Themes', blank=True)),
            ],
            options={
                'ordering': ['date'],
                'verbose_name': 'Work',
                'verbose_name_plural': 'Works',
            },
            bases=(models.Model,),
        ),
    ]
