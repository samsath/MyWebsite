
from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.conf import settings
from tastypie.api import Api
from .views import index

from .themes.resource import ThemeResources
from .file.resource import FileResources
from .portfolio.resource import LinkResources, WorkResource

v1_api = Api(api_name='v1')
v1_api.register(ThemeResources())
v1_api.register(FileResources())
v1_api.register(LinkResources())
v1_api.register(WorkResource())

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^$', index, name='home'),
)
