from .models import *
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from ..file.resource import FileResources
from ..themes.resource import ThemeResources


class BlogResources(ModelResource):
    cover = fields.ToOneField(FileResources, 'cover', full=True, null=True)
    content = fields.ToManyField(FileResources, 'content', full=True, null=True)
    themes = fields.ToManyField(ThemeResources, 'themes', full=True, null=True)

    class Meta:
        queryset = Blog.objects.all()
        resource_name = 'blog'
        allowed_methods = ['get',]
        filtering = {
            'id': ALL,
            'title': ALL,
            'slug': ALL,
            'created': ALL,
            'modified': ALL,
            'headline': ALL,
            'description': ALL,
            'date': ALL,
            'is_public': ALL,
            'content':  ALL_WITH_RELATIONS,
            'themes': ALL_WITH_RELATIONS,
            'cover': ALL_WITH_RELATIONS,
        }
        limit = 0
        max_limit = 0