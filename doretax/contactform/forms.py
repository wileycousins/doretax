class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    telephone = forms.EmailField(required=False)
    comments = forms.CharField()