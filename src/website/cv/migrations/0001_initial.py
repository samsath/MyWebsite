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
            name='CV',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'Title')),
                ('right', models.TextField(null=True, verbose_name='Description Right', blank=True)),
                ('headline', models.TextField(null=True, verbose_name='Headline', blank=True)),
                ('left', models.TextField(null=True, verbose_name='Description left', blank=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('institution', models.CharField(max_length=255, verbose_name=b'institution')),
                ('course', models.CharField(max_length=255, verbose_name=b'course')),
                ('start', models.DateField(null=True, verbose_name='Start', blank=True)),
                ('end', models.DateField(null=True, verbose_name='End', blank=True)),
                ('headline', models.TextField(null=True, verbose_name='Headline', blank=True)),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('sort_order', models.IntegerField(null=True, verbose_name='Sort order', blank=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
            ],
            options={
                'ordering': ['sort_order'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=255, verbose_name=b'Company')),
                ('title', models.CharField(max_length=255, verbose_name=b'Job title')),
                ('start', models.DateField(null=True, verbose_name='Start', blank=True)),
                ('end', models.DateField(null=True, verbose_name='End', blank=True)),
                ('headline', models.TextField(null=True, verbose_name='Headline', blank=True)),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('sort_order', models.IntegerField(null=True, verbose_name='Sort order', blank=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
            ],
            options={
                'ordering': ['sort_order'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'Title')),
                ('slug', django_extensions.db.fields.AutoSlugField(editable=False, populate_from=(b'title',), blank=True, unique=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cv',
            name='education',
            field=models.ManyToManyField(to='cv.Education', null=True, verbose_name=b'Education', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cv',
            name='job',
            field=models.ManyToManyField(to='cv.Jobs', null=True, verbose_name=b'Jobs', blank=True),
            preserve_default=True,
        ),
    ]
