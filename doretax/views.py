from datetime import datetime
from django.core.context_processors import csrf
from django.http import Http404
from django.shortcuts import render_to_response, Http404
from django.views.generic.simple import redirect_to
from doretax import settings
from doretax.biz.models import BusinessDetail, Association, Service

# load the basic contact info for Dore' & Company
contact = BusinessDetail.objects.get(name="Dore' & Company") 
if not contact:
    contact = BusinessDetail.objects.all()[0]

common_args = {
               'STATIC_URL' : settings.STATIC_URL,
               'contact' : contact,
               'base_template' : 'base.html',
               } 
 
def home(request, ajax):
    args = common_args.copy()    
    args['year'] = datetime.now().year
    args['assocs'] = Association.objects.professional()
    if ajax:
        args['base_template'] = "base-ajax.html"
    return render_to_response('home.html', args)
    
def about(request, ajax):
    args = common_args.copy()    
    args['year'] = datetime.now().year
    args['services'] = Service.objects.all()
    if ajax:
        args['base_template'] = "base-ajax.html"
    return render_to_response('about.html', args)
    
def client_center(request, ajax):    
    args = common_args.copy()    
    args['year'] = datetime.now().year
    if ajax:
        args['base_template'] = "base-ajax.html"
    return render_to_response('client-center.html', args)
    
def community(request, ajax):
    args = common_args.copy()    
    args['year'] = datetime.now().year
    if ajax:
        args['base_template'] = "base-ajax.html"
    return render_to_response('community.html', args)
    
def contact(request, ajax):
    args = common_args.copy()   
    args['year'] = datetime.now().year
    if ajax:
        args['base_template'] = "base-ajax.html"
    args.update(csrf(request))
    return render_to_response('contact.html', args)

def remove_slash(request, url):
    if url.endswith('/'):
        return redirect_to(request, '/' + url.rstrip('/'))
    else:
        raise Http404
    
def admin_add_slash(request):
    return redirect_to(request, request.path + '/')    
