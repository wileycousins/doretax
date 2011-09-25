from django.shortcuts import render_to_response
from doretax import settings
 
common_args = {
               'STATIC_URL' : settings.STATIC_URL,
               } 
 
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
