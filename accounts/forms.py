from django.contrib.auth.models import User
from django import forms

class UserLoginForm(forms.Form):
    email = forms.CharField(label="email", help_text=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserLoginForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ('email', 'password',)