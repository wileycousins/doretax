from django.shortcuts import render_to_response
 
def home(request):
    return render_to_response('home.html')
    
def about(request):
    return render_to_response('about.html')
    
def client_center(request):    
    return render_to_response('client-center.html')
    
def community(request):
    return render_to_response('community.html')
    
def contact(request):
    return render_to_response('contact.html')
