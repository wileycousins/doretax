from django.shortcuts import render_to_response
from doretax import settings
from django.core.context_processors import csrf
 
common_args = {
               'STATIC_URL' : settings.STATIC_URL,
               'base_template' : "base.html",
               } 

all_pages = ('about.html', 'contact.html', 'home.html', 'client-center.html', 'community.html')
 
def home(request):
    return render_to_response('home.html', common_args)
    
def about(request):
    return render_to_response('about.html', common_args)
    
def client_center(request):    
    return render_to_response('client-center.html', common_args)
    
def community(request):
    return render_to_response('community.html', common_args)
    
def contact(request):
    return render_to_response('contact.html', common_args)

def get(request, page):
#    if not request.is_ajax():
#        raise Http404
    args = {}
    args.update(csrf(request))
    args['base_template'] = "base-ajax.html"
    if page == '' or page == '/':
        page = 'home'
    page = "%s.html" % page
    if page in all_pages:
        return render_to_response('%s' % page, args)
    else:
        raise Http404