from django import forms
from django.contrib.localflavor.us.forms import USPhoneNumberField

class ContactForm(forms.Form):
    """
    A basic contact form to validate against.
    """
    name = forms.CharField()
    email = forms.EmailField()
    telephone = USPhoneNumberField(required=False)
    comments = forms.CharField()