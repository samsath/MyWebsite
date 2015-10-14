from django import forms
from django.contrib.admin.widgets import AdminTextInputWidget
from website.colorpicker import color_validator
from website.colorpicker.widgets import ColorInput


class ColorField(forms.CharField):
    default_validators = list(forms.CharField.default_validators) + [color_validator]
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('widget', ColorInput)
        if kwargs['widget'] == AdminTextInputWidget or \
            kwargs['widget'].__class__ == AdminTextInputWidget:
            kwargs['widget'] = ColorInput
        kwargs.setdefault('initial', '#000000')
        super(ColorField, self).__init__(*args, **kwargs)

    def clean(self, value):
        return value.strip()
