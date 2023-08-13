from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    class Meta:
        username = forms.CharField(max_length=60, label="User name")
        password = forms.CharField(
            max_length=60, widget=forms.PasswordInput, label="Password"
        )


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
