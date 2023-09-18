from django import forms

class UserRegistrationsForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
