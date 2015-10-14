from django.db import models
from website.colorpicker import forms
from website.colorpicker import color_validator


class ColorField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['validators'] = list(kwargs.setdefault('validators', []))
        kwargs['validators'].append(color_validator)
        kwargs.setdefault('max_length', 10)
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, form_class=forms.ColorField, **kwargs):
        return super(ColorField, self).formfield(form_class=form_class, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(ColorField, self).deconstruct()
        del kwargs["max_length"]
        return name, path, args, kwargs

