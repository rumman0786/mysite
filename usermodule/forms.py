from django.forms import ModelForm
from django.contrib.auth.models import User
from usermodule.models import UsermoduleProfile

# Create the form class.
class UsermoduleProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')