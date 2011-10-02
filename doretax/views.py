from datetime import datetime
from django.core.context_processors import csrf
from django.http import Http404
from django.shortcuts import render_to_response, Http404
from django.views.generic.simple import redirect_to
from doretax import settings
from doretax.biz.models import BusinessDetail, Association, Service, Link

#def doretax_404(request):

def get_contact():
    "load the basic contact info for Dore' & Company"
    contact = BusinessDetail.objects.get(name="Dore' & Company") 
    if not contact:
        contact = BusinessDetail.objects.all()[0]
    return contact

common_args = {
               'STATIC_URL' : settings.STATIC_URL,
               'base_template' : 'base.html',
               } 
 
def home(request, ajax):
    args = common_args.copy()
    args['year'] = datetime.now().year
    args['contact'] = get_contact()
    args['assocs'] = Association.objects.professional()
    if ajax:
        args['base_template'] = "base-ajax.html"
    return render_to_response('home.html', args)
    
def about(request, ajax):
    args = common_args.copy()    
    args['year'] = datetime.now().year
    args['contact'] = get_contact()
    args['services'] = Service.objects.all()
    if ajax:
        args['base_template'] = "base-ajax.html"
    return render_to_response('about.html', args)
    
def client_center(request, ajax):    
    args = common_args.copy()    
    args['year'] = datetime.now().year
    args['contact'] = get_contact()
    args['links'] = Link.objects.client()
    if ajax:
        args['base_template'] = "base-ajax.html"
    return render_to_response('client-center.html', args)
    
def community(request, ajax):
    args = common_args.copy()    
    args['year'] = datetime.now().year
    args['contact'] = get_contact()
    args['assocs'] = Association.objects.civic()
    args['links'] = Link.objects.community()
    if ajax:
        args['base_template'] = "base-ajax.html"
    return render_to_response('community.html', args)
    
def contact(request, ajax):
    args = common_args.copy()   
    args['contact'] = get_contact()
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

if settings.DEBUG:
    def four_oh_four(request, ajax):
        print 'foo'
        args = common_args.copy()   
        args['contact'] = get_contact()
        args['year'] = datetime.now().year
        if ajax:
            args['base_template'] = "base-ajax.html"
        args.update(csrf(request))
        return render_to_response('404.html', args)

    def five_oh_oh(request, ajax):
        args = common_args.copy()   
        args['contact'] = get_contact()
        args['year'] = datetime.now().year
        if ajax:
            args['base_template'] = "base-ajax.html"
        args.update(csrf(request))
        return render_to_response('500.html', args)


def contact_request(request):
    if request.method != "POST":
        raise Http404
    name = request.POST["name"]
    email = request.POST["email"]
    telephone = request.POST["telephone"]
    comments = request.POST["comments"]
    now = datetime.datetime.now()
    message = """
On %s, %s sent the following message: 

    %s
    
Contact Information:
email: %s
phone: %s
""" % (now, name, comments, email, telephone) 
    if not settings.IS_DEV:
        #send_mail(subject, message, from_email, recipient_list, fail_silently=False, auth_user=None, auth_password=None, connection=None)
        send_mail("Dore' & Company Contact Form from %s" % name, message, '"%s" <%s>' % (name, email), ['contact.form@doretax.com'], fail_silently=False)
        send_mail("Dore' & Company ", auto_response(name, message), '"Decode72" <hello@decode72.com>', [email], fail_silently=False)
    return HttpResponse("""Hi %s and thanks for contacting us. We'll get back with you shortly.""" % name)

def auto_response(name, message):
    return """
Hi %s!,

We received your message and will get back with you shortly. 
If you have no idea what we're talking about then someone probably used your email address in our contact form. 
If this is the case we most sincerely apologize.   

Cheers,

Decode72
http://decode72.com

--------------------------------------------------------------------------------
%s
""" % (name, message)
