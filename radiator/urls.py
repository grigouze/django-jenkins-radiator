from django.conf.urls.defaults import patterns

urlpatterns = patterns('radiator.views',
    (r'^$', 'index'),
    (r'^builds$', 'builds'),
)
