from django import forms

class ContactRequestForm(forms.Form):
    """A client's contact request form."""

    name = forms.CharField(max_length=12)
    phone = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    public_id = forms.CharField(max_length=9, widget=forms.HiddenInput())
    message = forms.CharField(max_length=255)
    