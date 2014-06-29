# -*- coding: utf-8 -*-

from __future__ import absolute_import

from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = patterns('jane.documents.views',
    url(r'^rest/(?P<resource_type>\w+)/$',
        view='rest_records_list',
        name='rest_records_list'),
    url(r'^rest/(?P<resource_type>\w+)/(?P<pk>[0-9]+)/$',
        view='rest_record_detail',
        name='rest_record_detail'),
    url(r'^rest/(?P<resource_type>\w+)/(?P<index_id>[0-9]+)/'
        '(?P<attachment_id>[0-9]+)/$',
        view='rest_attachment_view',
        name='rest_attachment_view'),
    url(r'^documents/(?P<resource_type>[-\w]+)/geojson',
        view='geojson',
        name='geojson'),
    url(r'^documents/(?P<resource_type>[-\w]+)/',
        view='test',
        name='test'),
)

urlpatterns = format_suffix_patterns(urlpatterns)

# XXX: currently fails for initial syncdb
try:
    from .plugins import initialize_plugins
    available_plugins = initialize_plugins()
except:
    pass
