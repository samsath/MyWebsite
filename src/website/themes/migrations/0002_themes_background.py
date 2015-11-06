# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import re
import website.colorpicker.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='themes',
            name='background',
            field=website.colorpicker.fields.ColorField(blank=True, null=True, validators=[django.core.validators.RegexValidator(regex=re.compile(b'^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$'), message='Enter a valid color.', code=b'invalid_color'), django.core.validators.RegexValidator(regex=re.compile(b'^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$'), message='Enter a valid color.', code=b'invalid_color'), django.core.validators.RegexValidator(regex=re.compile(b'^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$'), message='Enter a valid color.', code=b'invalid_color')]),
            preserve_default=True,
        ),
    ]
