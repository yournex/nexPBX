from django.conf.urls.defaults import patterns, include, url


from  views import index
urlpatterns = patterns('',
    url(r'^', index),
    
)

