from django import forms

class SignDocForm(forms.Form):
    file = forms.FileField()
    password = forms.CharField(widget=forms.PasswordInput)
    share = forms.CharField(required=False)

class VerifyDocForm(forms.Form):
    file = forms.FileField()
