from django.core.context_processors import csrf
from django.http import Http404
from django.shortcuts import render_to_response, redirect
from doretax import settings
 
all_pages = ('about.html', 'contact.html', 'home.html', 'client-center.html', 'community.html')
 
def default(request, page):
    args = {
            'STATIC_URL' : settings.STATIC_URL,
            'base_template' : "base.html",
            }
    args.update(csrf(request))
    if page.endswith('/'):
        return check_for_slash(request, page)
    if page == '':
        page = 'home'
    page = "%s.html" % page
    if page in all_pages:
        return render_to_response('%s' % page, args)
    else:
        raise Http404

def get(request, page):
    if not request.is_ajax():
        raise Http404
    args = {
            'STATIC_URL' : settings.STATIC_URL,
            'base_template' : "base-ajax.html",
            }
    args.update(csrf(request))
    if page.endswith('/'):
        page = page[:-1]
    if page == '':
        page = 'home'
    page = "%s.html" % page
    if page in all_pages:
        return render_to_response('%s' % page, args)
    else:
        raise Http404
    
def check_for_slash(request, page):
    #return redirect('default', {page=page[:-1] : request=request})
    raise Http404
    