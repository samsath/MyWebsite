from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import (AutoSlugField, CreationDateTimeField, ModificationDateTimeField)
from ..colorpicker.fields import ColorField

class Themes(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    sort_value = models.IntegerField(blank=True, null=True)
    is_public = models.BooleanField(default=False)
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()
    background = ColorField(null=True, blank=True)
    slug = AutoSlugField(populate_from=('title',), unique=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering =['sort_value',]
        verbose_name = _('Themes')
        verbose_name_plural = _('Themes')
