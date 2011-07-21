from django.conf.urls.defaults import patterns, include, url

import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nexPBX.views.home', name='home'),
    # url(r'^nexPBX/', include('nexPBX.foo.urls')),

    url(r'^(?P<protocol>\w+)/add/$', views.add),
     (r'^polls/(?P<poll_id>\d+)/$', 'views.add'),
)
