from django.conf.urls.defaults import *

tags = ['python','ruby','django']

urlpatterns = patterns('django.views.generic.simple',
    (r'^$','direct_to_template', {'template': 'sample.html','extra_context':{'tags':tags},}),
)
