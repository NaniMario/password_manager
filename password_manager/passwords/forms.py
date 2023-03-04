from django.forms import ModelForm
from .models import UserPassword

class PasswordForm(ModelForm):
    class Meta:
        model = UserPassword
        fields = ('app', 'password')

