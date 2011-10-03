from django import forms
from django.contrib.localflavor.us.forms import USPhoneNumberField

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    telephone = USPhoneNumberField(required=False)
    comments = forms.CharField()