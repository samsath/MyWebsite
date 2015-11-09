from .models import *
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS


class EducationResources(ModelResource):
    class Meta:
        queryset = Education.objects.all()
        resource_name = 'education'
        allowed_methods = ['get',]
        limit = 0
        max_limit = 0
        filtering = {
            'id': ALL,
            'institution': ALL,
            'course': ALL,
            'start': ALL,
            'end': ALL,
            'headline': ALL,
            'description': ALL,
            'sort_order': ALL,
            'created': ALL,
            'modified': ALL,
            'url': ALL
        }


class JobsResources(ModelResource):
    class Meta:
        queryset = Jobs.objects.all()
        resource_name = 'jobs'
        allowed_methods = ['get',]
        limit = 0
        max_limit = 0
        filtering = {
            'id': ALL,
            'company': ALL,
            'start': ALL,
            'end': ALL,
            'headline': ALL,
            'description': ALL,
            'sort_order': ALL,
            'created': ALL,
            'modified': ALL,
            'url': ALL
        }


class SkillResources(ModelResource):
    class Meta:
        queryset = Skills.objects.all()
        resource_name = 'skills'
        limit = 0
        max_limit = 0
        filtering = {
            'id': ALL,
            'title': ALL,
            'slug': ALL,
            'created': ALL,
            'modified': ALL
        }


class CVResources(ModelResource):
    class Meta:
        queryset = CV.objects.all()
        resource_name = 'cv'
        allowd_methods = ['get',]
        limit = 0
        max_limit = 0
        filtering = {
            'id':ALL,
            'title':ALL,
            'created':ALL,
            'modified':ALL,
            'right':ALL,
            'left':ALL
        }