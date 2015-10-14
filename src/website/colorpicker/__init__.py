import re
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


color_validator = RegexValidator(
    regex=re.compile(r'^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$'),
    message=_('Enter a valid color.'),
    code='invalid_color')
