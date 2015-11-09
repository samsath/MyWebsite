__author__ = 'sam'
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import (AutoSlugField, CreationDateTimeField, ModificationDateTimeField)
from ..file.models import File
from ..colorpicker.fields import ColorField
from ..themes.models import Themes


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()
    slug = AutoSlugField(populate_from=('title',), unique=True)

    content = models.ManyToManyField(File, verbose_name='Content', blank=True, null=True, related_name='blog_content')
    cover = models.ForeignKey(File, verbose_name='Cover', blank=True, null=True, related_name='blog_image')
    themes = models.ManyToManyField(Themes, verbose_name='Themes', blank=True, null=True)

    headline = models.TextField(_('Headline'), blank=True, null=True)
    description = models.TextField(_('Description'), blank=True, null=True)
    date = models.DateField(_('Date'), blank=True, null=True)
    is_public = models.BooleanField(default=False)

    background = ColorField(null=True, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering =['date',]
        verbose_name = _('Blog')
        verbose_name_plural = _('Blog')