from django.conf.urls.defaults import *
from django.contrib import admin 
from django.views.generic.simple import redirect_to, direct_to_template
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'views.home'),
    (r'^about$', 'views.about'),
    (r'^client-center$', 'views.client_center'),
    (r'^community$', 'views.community'),
    (r'^contact$', 'views.contact'),
    
    (r'^favicon.ico$', redirect_to, {'url': '/site_media/static/images/fav.ico'}),
    (r'^robots.txt$', direct_to_template, {'template':'robots.txt', 'mimetype':'text/plain'}),
    (r'^sitemap.txt$', direct_to_template, {'template':'sitemap.txt', 'mimetype':'text/plain'}),
    # (r'^doretax/', include('doretax.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
