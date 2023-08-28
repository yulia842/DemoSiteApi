from django import forms
from django.core.validators import EmailValidator
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"