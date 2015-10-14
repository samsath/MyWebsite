from .models import *
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS


class FileResources(ModelResource):

    def dehydrate(self, bundle):
        bundle.data['url'] = bundle.obj.get_url()
        return bundle

    class Meta:
        queryset = File.objects.all()
        resource_name = 'files'
        allowed_methods = ['get',]
        always_return_data = True
        filtering = {
            'id':ALL,
            'title': ALL,
            'slug': ALL,
            'created': ALL,
            'modified': ALL,
            'type': ALL,
        }
        limit = 0
        max_limit = 0
