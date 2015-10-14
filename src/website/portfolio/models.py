from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import (AutoSlugField, CreationDateTimeField, ModificationDateTimeField)

from ..colorpicker.fields import ColorField

from ..file.models import File
from ..themes.models import *


class Links(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()
    slug = AutoSlugField(populate_from=('title',), unique=True)
    file = models.ForeignKey(File, verbose_name='File', blank=True, null=True)
    url = models.URLField(_('Url'), blank=True, null=True)
    background = ColorField(null=True, blank=True)
    foreground = ColorField(null=True, blank=True)

    def __unicode__(self):
        return self.title

    def get_type(self):
        if self.url and self.file:
            return 'both'
        elif self.url:
            return 'url'
        elif self.file:
            return self.file.type
        else:
            return None

    class Meta:
        verbose_name = _('Link')
        verbose_name_plural = _('Links')


class Work(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()
    slug = AutoSlugField(populate_from=('title',), unique=True)

    content = models.ManyToManyField(File, verbose_name='Content', blank=True, null=True, related_name='work_content')
    cover = models.ForeignKey(File, verbose_name='Cover', blank=True, null=True, related_name='cover_image')
    themes = models.ManyToManyField(Themes, verbose_name='Themes', blank=True, null=True)
    links = models.ManyToManyField(Links, verbose_name='Links', blank=True, null=True)
    related = models.ManyToManyField('self', verbose_name='Related Work', blank=True, null=True, related_name='related_work')

    headline = models.TextField(_('Headline'), blank=True, null=True)
    description = models.TextField(_('Description'), blank=True, null=True)
    date = models.DateField(_('Date'), blank=True, null=True)
    is_public = models.BooleanField(default=False)

    background = ColorField(null=True, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering =['date',]
        verbose_name = _('Work')
        verbose_name_plural = _('Works')
