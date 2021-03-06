from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nexPBX.views.home', name='home'),
    # url(r'^nexPBX/', include('nexPBX.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^protocol/', include('Protocols.urls')),
    url(r'^dojango/', include('dojango.urls')),
    url(r'^', include('nexPages.urls')),
    
)

#urlpatterns += patterns('',
#    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/path/to/media'}),
#    )
