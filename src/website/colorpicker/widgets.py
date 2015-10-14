from django.conf import settings
from django.forms.widgets import TextInput
from django.utils.safestring import mark_safe


class ColorInput(TextInput):
    class Media:
        css = {
            'screen': (
                settings.STATIC_URL + 'colorpicker/farbtastic.css',
            ),
        }
        js = (
            settings.STATIC_URL + 'colorpicker/colorpicker.js',
            settings.STATIC_URL + 'colorpicker/farbtastic.js',
        )

    def render(self, name, value, attrs=None):
        html = []
        html.append('<div id="%s_colorpicker" style="float:left;"></div>' % attrs['id'])
        html.append(super(ColorInput, self).render(name, value, attrs))
        html.append('<script type="text/javascript">colorpicker.jQuery(document).ready(function ($) {')
        html.append('$("#%s_colorpicker").farbtastic("#%s");' % (attrs['id'], attrs['id']))
        html.append('});</script>')
        return mark_safe(u'\n'.join(html))
