from datetime import datetime
from django.core.mail import send_mail
from django.shortcuts import Http404, render_to_response, HttpResponse
from django.template import Context, Template
from django.template.loader import get_template
from forms import ContactForm

#invalid_email = 
#
#validation = {
#    "invalid_email" : invalid_email,
#    "required_email" : required_email,
#    "required_message" : required_message,
#    "required_name" : required_name,
#}

def render_subject(data):
    """
    Render the subject line using the subject.html template.
    data - expected to be cleaned form data
    """
    t = get_template('subject.html')
    c = Context(data)
    return t.render(c)
 
    
def render_message(data):
    """
    Render the message using the email-webmaster.html template.
    data - expected to be cleaned form data
    """
    data['now'] = datetime.now()
    t = get_template('email-webmaster.html')
    c = Context(data)
    return t.render(c)
            
def render_sender(data):            
    """
    Return the sender in the standard email format.
    e.g. "John Doe" <john@doe.com>
    data - expected to be cleaned form data
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
                send_mail(subject, message, sender, recipients, fail_silently=False) #,auth_user=None, auth_password=None, connection=None)
            
            return render_to_response('success.html', form.cleaned_data)
        else:
            return render_to_response('fail.html')
    else:
        raise Http404
    
