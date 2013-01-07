# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api
from course_catalog.api.resources import SubjectResource, CourseResource

v01_api = Api(api_name='v0.1')
v01_api.register(SubjectResource())
v01_api.register(CourseResource())

urlpatterns = patterns('',

    # Uncomment the next line to enable the SOLUS screen scraper
    url(r'^solus_scraper/', include('solus_scraper.urls')),

    # Uncomment the next line to enable checking of enrollment
    url(r'^enrollment/', include('enrollment.urls')),
    (r'^api/', include(v01_api.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('course_catalog.urls')),
)
