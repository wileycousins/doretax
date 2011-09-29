from django.core.context_processors import csrf
from django.http import Http404
from django.shortcuts import render_to_response, redirect
from doretax import settings
from doretax.biz.models import BusinessDetail

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
    if ajax:
        args['base_template'] = "base-ajax.html"
    return render_to_response('home.html', args)
    
def about(request, ajax):
    args = common_args.copy()    
    args['base_template'] = "base.html"
    if ajax:
        args['base_template'] = "base-ajax.html"
        
    return render_to_response('about.html', args)
    
def client_center(request, ajax):    
    args = common_args.copy()    
    if ajax:
        args['base_template'] = "base-ajax.html"
    return render_to_response('client-center.html', args)
    
def community(request, ajax):
    args = common_args.copy()    
    if ajax:
        args['base_template'] = "base-ajax.html"
    return render_to_response('community.html', args)
    
def contact(request, ajax):
    args = common_args.copy()   
    print 'shals' 
    if ajax:
        args['base_template'] = "base-ajax.html"
    return render_to_response('contact.html', args)
