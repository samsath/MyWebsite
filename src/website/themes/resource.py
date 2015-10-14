from .models import *
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS


class ThemeResources(ModelResource):
    class Meta:
        queryset = Themes.objects.filter(is_public=True)
        resource_name = 'themes'
        allowed_methods = ['get',]
        always_return_data = True
        filtering = {
            'id':ALL,
            'title':ALL,
            'sort_value':ALL
        }
        limit = 0
        max_limit = 0
