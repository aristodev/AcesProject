from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(widget=forms.TextInput(attrs={'pattern':'^01[0-2]{1}[0-9]{8}', 'title':'Enter an Egyptian mobile number '}))
    class Meta:
        model = User
        fields = ("email","password", "phone")


class loginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ("email","password")
