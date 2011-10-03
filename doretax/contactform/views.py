from datetime import datetime
from django.core.mail import send_mail
from django.shortcuts import Http404, render_to_response
from django.template import Context, Template, RequestContext, loader
from forms import ContactForm

def render_subject(data):
    name = form.cleaned_data['name']
    "Dore' & Company Contact Form from %s" % name, message,
    
def render_message(data):
    name = form.cleaned_data['name']
    from_email = form.cleaned_data['email']
    telephone = form.cleaned_data['telephone']
    message = form.cleaned_data['comments']
    datetime = datetime.now()
            t = loader.get_template("email-webmaster.html")
            
def render_sender(data):            
    """
    Return the sender in the standard email format.
    e.g. "John Doe" <john@doe.com>
    """
    return '"%s" <%s>' % (data['name'], data['email'])
            
def submit(request, recipients=None, debug=False):
    """
    Submit the contact form request to the specified recipients.
    If debug is True, do everything but actually send the message.
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            sender = render_sender(form.cleaned_data)
            subject = render_subject(form.cleaned_data) 
            message = render_message(form.cleaned_data)
            
            if not debug:
                #send_mail(subject, message, from_email, recipient_list, fail_silently=False, auth_user=None, auth_password=None, connection=None)
                send_mail( fail_silently=False)
                send_mail(subject, message, sender, recipients)
            
            return render_to_response('success.html')
        else:
            return render_to_response('fail.html')
    else:
        raise Http404
    
