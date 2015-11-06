from .models import *
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from ..file.resource import FileResources
from ..themes.resource import ThemeResources


class LinkResources(ModelResource):
    file = fields.ToOneField(FileResources, 'file', full=True, null=True)

    class Meta:
        queryset = Links.objects.all()
        resource_name = 'links'
        allowed_methods = ['get',]
        filtering = {
            'id': ALL,
            'title': ALL,
            'slug': ALL,
            'created': ALL,
            'modified': ALL,
            'url': ALL
        }
        limit = 0
        max_limit = 0


class WorkResource(ModelResource):
    cover = fields.ToOneField(FileResources, 'cover', full=True, null=True)
    content = fields.ToManyField(FileResources, 'content', full=True, null=True)
    themes = fields.ToManyField(ThemeResources, 'themes', full=True, null=True)
    links = fields.ToManyField(LinkResources, 'links', full=True, null=True)
    related = fields.ToManyField('self', 'related', full=False, null=True)

    class Meta:
        queryset = Work.objects.filter(is_public=True)
        resource_name = 'work'
        allowed_methods = ['get',]
        limit = 0
        max_limit = 0
        filtering = {
            'id': ALL,
            'title': ALL,
            'slug': ALL,
            'created': ALL,
            'modified': ALL,
            'url': ALL
        }