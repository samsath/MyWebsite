from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import (AutoSlugField, CreationDateTimeField, ModificationDateTimeField)


class File(models.Model):
    FILE_CHOICE = (
        ('image', _('Image')),
        ('pdf', _('Pdf')),
        ('audio', _('Audio')),
        ('video', _('Video')),
        ('text', _('Text')),
    )

    title = models.CharField(max_length=255, verbose_name="Title")
    file = models.FileField()
    type = models.CharField(_('Type'), max_length=50, choices=FILE_CHOICE, blank=True)
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()
    slug = AutoSlugField(populate_from=('title',), unique=True)

    def __unicode__(self):
        return self.title

    def get_url(self):
        return str(self.file.url)

    class Meta:
        ordering =['modified',]
        verbose_name = _('File')
        verbose_name_plural = _('File')
