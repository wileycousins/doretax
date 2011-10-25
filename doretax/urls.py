from django.conf.urls.defaults import *
from django.contrib import admin 
from django.views.generic.simple import redirect_to, direct_to_template
from doretax.settings import DEBUG
from doretax.settings import AJAX_VIEW_PREFIX as ajax
admin.autodiscover()

# custom 404 and 500 handlers
handler404 = 'views.doretax_404'
handler500 = 'views.doretax_500'

# basic stuff
urlpatterns = patterns('',
    (r'^favicon.ico$', redirect_to, {'url': '/site_media/static/images/fav.ico'}),
    (r'^admin/', include(admin.site.urls)),
#    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^robots.txt$', direct_to_template, {'template':'robots.txt', 'mimetype':'text/plain'}),
    (r'^sitemap.txt$', direct_to_template, {'template':'sitemap.txt', 'mimetype':'text/plain'}),
)

# public pages w/ajax support
urlpatterns += patterns('',
    (r'^(?P<ajax>(%s)?)$' % ajax, 'views.home'),
    (r'^(?P<ajax>(%s)?)about$' % ajax, 'views.about'),
    (r'^(?P<ajax>(%s)?)client-resources' % ajax, 'views.client_resources'),
    (r'^(?P<ajax>(%s)?)community$' % ajax, 'views.community'),
    (r'^(?P<ajax>(%s)?)contact$' % ajax, 'views.contact'),
    (r'^(?P<ajax>(%s)?)privacy$' % ajax, 'views.privacy'),
)

if DEBUG:
    # let us test out missing page and server error when debugging
    urlpatterns += patterns('',
        (r'^404$', 'views.doretax_404'),
        (r'^500$', 'views.doretax_500'),
    )

# oh why oh why isn't there a REMOVE_SLASH option...
urlpatterns += patterns('',
    (r'^admin$', 'views.admin_add_slash'),
    (r'^(?P<url>.*)$', 'views.remove_slash'),
)

