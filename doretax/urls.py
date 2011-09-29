from django.conf.urls.defaults import *
from django.contrib import admin 
from django.views.generic.simple import redirect_to, direct_to_template
from doretax.settings import AJAX_VIEW_PREFIX as ajax
admin.autodiscover()

# basic stuff
urlpatterns = patterns('',
    (r'^favicon.ico$', redirect_to, {'url': '/site_media/static/images/fav.ico'}),
    (r'^admin/', include(admin.site.urls)),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^robots.txt$', direct_to_template, {'template':'robots.txt', 'mimetype':'text/plain'}),
    (r'^sitemap.txt$', direct_to_template, {'template':'sitemap.txt', 'mimetype':'text/plain'}),
)

# public pages w/ajax support
urlpatterns += patterns('',    
    (r'^(?P<ajax>(%s)?)$' % ajax, 'views.home'),
    (r'^(?P<ajax>(%s)?)about$' % ajax, 'views.about'),
    (r'^(?P<ajax>(%s)?)client-center$' % ajax, 'views.client_center'),
    (r'^(?P<ajax>(%s)?)community$' % ajax, 'views.community'),
    (r'^(?P<ajax>(%s)?)contact$' % ajax, 'views.contact'),
)
