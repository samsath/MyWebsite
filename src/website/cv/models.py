__author__ = 'sam'
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import (AutoSlugField, CreationDateTimeField, ModificationDateTimeField)


class Education(models.Model):
    institution = models.CharField(max_length=255, verbose_name="institution")
    course = models.CharField(max_length=255, verbose_name="course")
    start = models.DateField(_('Start'), blank=True, null=True)
    end = models.DateField(_('End'), blank=True, null=True)
    headline = models.TextField(_('Headline'), blank=True, null=True)
    description = models.TextField(_('Description'), blank=True, null=True)
    sort_order = models.IntegerField(_('Sort order'), blank=True, null=True)
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    def __unicode__(self):
        return "{0} at {1}".format(self.course, self.institution)

    class Meta:
        ordering = ['sort_order',]


class Jobs(models.Model):
    company = models.CharField(max_length=255, verbose_name="Company")
    title = models.CharField(max_length=255, verbose_name="Job title")
    start = models.DateField(_('Start'), blank=True, null=True)
    end = models.DateField(_('End'), blank=True, null=True)
    headline = models.TextField(_('Headline'), blank=True, null=True)
    description = models.TextField(_('Description'), blank=True, null=True)
    sort_order = models.IntegerField(_('Sort order'), blank=True, null=True)
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    def __unicode__(self):
        return "{0} at {1}".format(self.title, self.company)

    class Meta:
        ordering = ['sort_order',]


class Skills(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    slug = AutoSlugField(populate_from=('title',), unique=True)
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    def __unicode__(self):
        return self.title


class CV(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()
    right = models.TextField(_('Description Right'), blank=True, null=True)
    headline = models.TextField(_('Headline'), blank=True, null=True)
    left = models.TextField(_('Description left'), blank=True, null=True)
    education = models.ManyToManyField(Education, verbose_name='Education', blank=True, null=True)
    job = models.ManyToManyField(Jobs, verbose_name='Jobs', blank=True, null=True)

    def __unicode__(self):
        return self.title