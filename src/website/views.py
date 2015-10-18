__author__ = 'sam'

from django.template.response import TemplateResponse

def index(request):
    return TemplateResponse(request, 'base.html', {})
