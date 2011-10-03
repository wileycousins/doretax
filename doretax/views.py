from datetime import datetime
from django import http
from django.core.context_processors import csrf
from django.http import Http404
from django.shortcuts import render_to_response, Http404
from django.template import Context, Template, RequestContext, loader
from django.views.generic.simple import redirect_to
from django.views.decorators.csrf import requires_csrf_token
from doretax import settings
from doretax.biz.models import BusinessDetail, Association, Service, Link
from doretax.contactform.forms import ContactForm

def contact_info():
    contact = BusinessDetail.objects.get(name="Dore' & Company") 
    if not contact:
        contact = BusinessDetail.objects.all()[0]
    return contact

def common_args(ajax=False):
    """
    The common arguments for all doretax views.
    ajax: Describes if the args are for an ajax request.
    
    STATIC_URL: static url from settings
    year: the year at the time of request
    contact: doretax business contact information
    base_template: the default base template  
    """
    args = {
               'STATIC_URL' : settings.STATIC_URL,
               'year' : datetime.now().year,
               'contact': contact_info(),
               'base_template' : 'base.html',
           }
    if ajax:
        args['base_template'] = "base-ajax.html"
    return args 
    
# This can be called when CsrfViewMiddleware.process_view has not run, therefore
# need @requires_csrf_token in case the template needs {% csrf_token %}.
@requires_csrf_token
def doretax_404(request, template_name='404.html'):
    """ 
    404 handler for doretax.

    Templates: `404.html`
    Context:
        common_args from doretax
        request_path
            The path of the requested URL (e.g., '/app/pages/bad_page/')
        
    """
    t = loader.get_template(template_name) # You need to create a 404.html template.
    args = common_args()
    args['request_path'] = request.path
    return http.HttpResponseNotFound(t.render(RequestContext(request, args)))


@requires_csrf_token
def doretax_500(request, template_name='500.html'):
    """ 
    500 error handler for doretax.

    Templates: `500.html`
    Context: common_args from doretax
    """
    t = loader.get_template(template_name) # You need to create a 500.html template.
    return http.HttpResponseServerError(t.render(Context(common_args())))
 
def home(request, ajax):
    args = common_args(ajax)
    args['assocs'] = Association.objects.professional()
    return render_to_response('home.html', args)
    
def about(request, ajax):
    args = common_args(ajax)    
    args['services'] = Service.objects.all()
    return render_to_response('about.html', args)
    
def client_center(request, ajax):    
    args = common_args(ajax)    
    args['links'] = Link.objects.client()
    return render_to_response('client-center.html', args)
    
def community(request, ajax):
    args = common_args(ajax)    
    args['assocs'] = Association.objects.civic()
    args['links'] = Link.objects.community()
    return render_to_response('community.html', args)
    
def contact(request, ajax):
    args = common_args(ajax)
    args.update(csrf(request))
    return render_to_response('contact.html', args)

def contact_request(request):
    return contactform.views.submit(request, [contact_info()['email']], settings.DEBUG)

def remove_slash(request, url):
    if url.endswith('/'):
        return redirect_to(request, '/' + url.rstrip('/'))
    else:
        raise Http404
    
def admin_add_slash(request):
    return redirect_to(request, request.path + '/')
