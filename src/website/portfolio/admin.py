from django.contrib import admin
from .models import *

class WorkSect(admin.ModelAdmin):
    filter_horizontal = ['related', 'links', 'themes']


admin.site.register(Links)
admin.site.register(Work, WorkSect)
