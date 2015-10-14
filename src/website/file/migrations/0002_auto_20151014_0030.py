# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='type',
            field=models.CharField(blank=True, max_length=50, verbose_name='Type', choices=[(b'image', 'Image'), (b'pdf', 'Pdf'), (b'audio', 'Audio'), (b'video', 'Video'), (b'text', 'Text')]),
            preserve_default=True,
        ),
    ]
