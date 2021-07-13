from django import forms
from django.forms import widgets
from .models import Contact

class CreateNewEmailSubscription(forms.Form):
    email = forms.EmailField(label="Email:", max_length=200)

class SubmitQuestion(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Contact
        fields= ['first_name', 'last_name', 'email', 'phone', 'state', 'message']

        widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'email': forms.EmailInput(),
            'phone': forms.TextInput(),
            'state': forms.TextInput(),
            'message': forms.Textarea(attrs={'placeholder': '200 character limit'})
        }