from django import forms

class CreateNewEmailSubscription(forms.Form):
    email = forms.EmailField(label="Email:", max_length=200)