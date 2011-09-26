from django.conf.urls.defaults import *
from django.contrib import admin 
from django.views.defaults import page_not_found
from django.views.generic.simple import redirect_to, direct_to_template
admin.autodiscover()

urlpatterns = patterns('',
    (r'^favicon.ico$', redirect_to, {'url': '/site_media/static/images/fav.ico'}),
    (r'^get/(?P<page>.*)/?$', 'views.get'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^$', 'views.default', {'page':'home'}),
    (r'^home$', page_not_found),
    (r'^robots.txt$', direct_to_template, {'template':'robots.txt', 'mimetype':'text/plain'}),
    (r'^sitemap.txt$', direct_to_template, {'template':'sitemap.txt', 'mimetype':'text/plain'}),
    (r'^admin/', include(admin.site.urls)),
    (r'^admin$', redirect_to, {'url': '/admin/'}),
    (r'^(?P<page>.*)$', 'views.default'), # make sure this is last as it will catch everything
)
