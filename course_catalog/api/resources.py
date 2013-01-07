from django.conf.urls import url
from tastypie import fields
from tastypie.resources import ModelResource, ALL_WITH_RELATIONS
from course_catalog.models import Course, Subject


class SubjectResource(ModelResource):
    class Meta:
        queryset = Subject.objects.all()
        allowed_methods = ['get']
        resource_name = 'subject'

    def __init__(self, *args, **kwargs):
        super(SubjectResource, self).__init__(*args, **kwargs)
        self.override_urls = self.prepend_urls # tastypie 0.9.11 likes override_urls, which is deprecated

    def prepend_urls(self):
        return [
            url(r'^(?P<resource_name>%s)/(?P<abbreviation>[\w\d_.-]+)/$' % self._meta.resource_name, self.wrap_view('dispatch_detail'), name='api_dispatch_detail'),
        ]


class CourseResource(ModelResource):
    subject = fields.ForeignKey(SubjectResource, 'subject')
    
    class Meta:
        queryset = Course.objects.all()
        allowed_methods = ['get']
        resource_name = 'course'
        filtering = {
            'subject': ALL_WITH_RELATIONS,
        }

    """
    def prepend_urls(self):
        return [
            url(r'^course/(?P<course_code>[\w\d_.-]+)/$', self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
        ]
    """
